create type public.staff_role as enum ('admin', 'reception');

create table public.staff_profiles (
  user_id uuid primary key references auth.users on delete cascade,
  name text not null,
  role public.staff_role not null default 'reception',
  active boolean not null default true,
  created_at timestamptz not null default now()
);

alter table public.staff_profiles enable row level security;
revoke all on public.staff_profiles from anon, authenticated;

-- Depois de criar a primeira usuária em Authentication > Users, conceda acesso:
-- insert into public.staff_profiles (user_id, name, role)
-- values ('UUID-DO-USUARIO', 'Nome da recepção', 'admin');
