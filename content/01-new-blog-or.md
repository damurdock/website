Title: New Blog and How it Works
Date: 2014-07-09 3:30 AM
Tags: admin, web, projects, deployment
Category: Projects
Slug: 01-new-blog-or
Author: Duncan Murdock

Joining the ranks of many up-and-coming twentysomething computer types, I've (finally) set up a personal blog. Hopefully, it will come to serve as a repository of the projects I've made and will make, as well as what I hope are useful insights and interesting anecdotes. One thing that seems sorely missing from many blogs is a description of how all the parts fit together. Making this blog was not a trivial task, and each part was chosen for a reason. So to help future blogmakers (and so I don't forget), here it is.

### The Parts 

__[Pelican](http://getpelican.com):__ A Python Static Site Generator (SSG)

__[pelican-bootstrap3](https://github.com/DandyDev/pelican-bootstrap3):__ A port of the Bootstrap3 theme framework to Pelican

__[Heroku](http://heroku.com):__ A Platform as a Service (PaaS) provider with a free tier and git-based deploy

__[Github](http://github.com):__ _The_ PaaS [Git](git-scm.com) provider

__[Travis](http://travis-ci.com):__ A free Continuous Integration (CI) provider, fed by Github

__[Cloudflare](http://cloudflare.com):__ A Content Delivery Network (CDN) with a free tier

__[Math Render Plugin For Pelican](https://github.com/barrysteyn/pelican_plugin-render_math):__ A MathJax plugin for Pelican

### Why Pelican?

SSGs are all the rage these days, and for good reason. They make lightweight websites that are easy to manage and can run almost anywhere. Pelican is based on Python (my favorite language) and has a simple theming archetecture, a buildpack for Travis, and lots of themes. Plus, it's super-simple to deploy and actively developed.

### Why pelican-bootstrap3?

Pelican-bootstrap3 brings the Bootstrap3 theme framework to Pelican. Bootstrap is _the_ framework these days, and powers a lot of the web as we know it. Seriously, just ctrl-f the source of your favorite sites for bootstrap.css and you'll see what I mean. More to the point, Bootstrap is pretty, includes glyphicons and fontawesome(so pretty glyphs all over the place), and is responsive. Responsive design, aside from being a huge buzzword, is very useful, because it means your pages are pretty _everywhere_, not just on the desktop.

### Why Heroku?

All of my previous attempts at hosting a website used nearlyfreespeech.net. NFSN is a great host, and I don't want to hate on them, but their price schedule makes it hard (for me, at least) to immediately scale. Say, for instance, I post something that makes it to hackaday and my site gets flooded (one can dream). If my cost excedes my deposited funds, then poof goes the website. Heroku, on the other hand, has limited resources, but it's free, and those resourses only scale if I want them to. Also, it's combatible with git, Pelican, and Travis nearly out of the box. The only real problem I can see is that the webserver sleeps after so long without being accessed. I could set up a script to ping the site every hour or so, but the few seconds of delay don't seem worth abusing Heroku's generosity.

### Why Github?

Github makes it easy to keep track of revisions. It also allows me to write posts online and commit them. That way, I can post from any computer with ease. It also hooks into Travis directly.

### Why Travis?

With Travis, all I have to do to update my site is push to the Github repo. Travis hooks in, builds the site, and deploys it to Heroku automatically. It's a little slow, but I can wait a few minutes to post, honestly.

### Why Cloudflare?

Cloudflare sits between my site and the rest of the internet, giving users fast cache access to static resources like images and css. It gives me a nice "panic button" in the unlikely event of a DDoS attack. Plus it has a very nice and easy to use DNS configurator.

### Why MathJax?

MathJax, via the Math Render Plugin For Pelican, lets me use math formulae and other \(\LaTeX\) expressions in posts. This lets me write about math and actually show the formulae without having to write the \(\LaTeX\) and render it to a picture. Then, you can actually copy it, zoom in and out, and search for it. Neat stuff.

So, that's the basics. I'm thinking of moving hosting to S3, but for now this is the setup. Let me know if you have any questions/comments/concerns.