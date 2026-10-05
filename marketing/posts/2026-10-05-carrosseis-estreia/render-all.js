const posts=require('./posts.json');
(async()=>{for(const post of posts) await require('./'+post.slug+'/render.js')();})().catch(error=>{console.error(error);process.exitCode=1});
