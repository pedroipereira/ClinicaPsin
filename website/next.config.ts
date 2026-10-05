import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async redirects(){return [
    {source:"/institutional/index.html",destination:"/",permanent:true},
    {source:"/institutional/profissionais/:slug.html",destination:"/profissionais/:slug",permanent:true},
    {source:"/institutional/blog/index.html",destination:"/blog",permanent:true},
    {source:"/institutional/blog/:slug.html",destination:"/blog/:slug",permanent:true},
  ]},
};

export default nextConfig;
