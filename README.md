# A Web Site About Me

Welcome! In this assignment, you will create a personal web site consisting of three distinct web pages:

- Your personal web site's home page: `index.html`
- A page about you: `about_me.html`
- An additional page with something more about you: `more_about_me.html`

These web pages must be published to the web by uploading them to your web root directory on the web server.

Some rules about each page follow.

On top of these requirements, you are welcome to add any additional content you believe will make this page compelling and interesting to someone finding it on the web. For example, include links to any places, topics, or organizations you mention in the text; add images, video, audio tracks, etc.

## Home Page

Create a home page for your personal web site and name it `index.html` - it will replace any existing file you have by that name.

This page must still meet the requirements of the UNIX Assignment, in addition to the following...

It must contain an **ordered list** of links to pages for each assignment in this class. You do not yet have to create pages for each assignment, but the links should be present on this home page. The names and file names of the web pages that you must link from your home page are, in order:

- UNIX Assignment (link to `index.html`)
- HTML Assignment (link to `about_me.html`)
- CSS Assignment (link to `index.html`)
- JQuery Assignment (link to `topic_of_interest.html`)
- User Experience Assignment (link to `user_experience_design.html`)
- Responsive Design Assignment (link to `index.html`)
- Bootstrap Assignment (link to `professional_site.html`)
- Photoshop Assignment (link to `photoshop.html`)
- Animated GIF Assignment (link to `animated_gif.html`)
- Digital Video Assignment (link to `video.html`)

Add any additional content you like before and/or after that list.

## About Me Page

Create a page about yourself, named `about_me.html`. Only share on this page whatever information you are comfortable sharing publicly.

**Heading**
Include an `<h1>` element with the title of this page.

**Sections**
Include discrete `<section>` elements for each of the following sections of this page.

- **My background** - tell us who you are and where you come from in this section.
- **My interests** - give us a sense of your interests in this section.

You must include the name of each section, exactly as written in the list above, placed within an `<h2>` element nested within the relevant `<section>` element. And each section must include at least one paragraph, written in a `<p>` element.

**Images**
You must include at least two images on this page using the `<img>` element. One of these images must be a photograph. You must be licensed to use these images and give credit to the image creator, if that is required by the copyright license the image is pulished under.

**Links**
This page must include a link to the next page, named `more_about_me.html`, as well as a link back to your site's home page, `index.html`. These must both be **relative links**, not absolute links.

At least one additional link should link to a page on a different web site. This must be an absolute link.

## More About Me Page

This page, named `more_about_me.html`, will hold content about some specific experiences you have had that you would like to share. Only share on this page whatever information you are comfortable sharing publicly.

**Heading**
Include an `<h1>` element with the title of this page.

**Section**
Include a discrete `<section>` element to hold the content about unique experiences you would like to share. This section should contain at least one paragraph in a `<p>` element. Feel free to add additional content.

**Images**
You must include at least two images on this page using the `<img>` element. These must be different from the images used on the `about_me.html` page. You must be licensed to use these images and give credit to the image creator, if that is required by the copyright license the image is pulished under.

**Links**
This page must include a link back to the general page about you, named `about_me.html`, as well as a link back to your site's home page, `index.html`. These must both be relative links, not absolute links.

At least one additional link should link to a page on a different web site. This must be an absolute link.

## Submit your work

In order to submit this assignment, you must publish it to the web and upload the code to GitHub.

### Upload the web page to a web server

Upload all files you have created to a web server. Your instructor will have given you instructions for how to do this.

Take note of the web address (URL) of your web page - this is the address that can be plugged into the address bar of any web browser for the web browser to load and display your web page.

### Add your web page's URL to the settings.json file

Make sure your name, NYU Net ID, and the exact URL of your web site's home page is placed into the `settings.json` file in the appropriate places. Make sure the URL works when plugged into a web browser beforehand.

### Submit your work on GitHub

You are now ready to submit this assignment. You can do so directly from Visual Studio Code with the following steps, in the indicated order:

1. Switch to the Source Control view in Visual Studio Code - this view will show you a list of the files you have modified.
1. In the "Message" text field towards the top-left, enter a unique message to yourself about what you have changed and, while still with the text field selected, type Command-Enter on Mac OS X, or Control-Enter on Windows, to "commit" the changes you've made with this custom message. If you forget to hit Command-Enter after typing the message, you can instead click the "..." button above the message field and click the "Commit all" option in the menu that appears.
1. Now, click the "..." button above the message field and click the "Push" option in the menu that appears - this will upload your changes to your personal code repository on GitHub.

You have now submitted your completed assignment. Your changes are now posted to GitHub.com, where the instructor and graders can access it. Your `settings.json` file has information about who you are and where we can view your page on the web.

You can verify all this yourself manually by visiting your repository on GitHub.com and making sure the code displayed there is what you submitted.
