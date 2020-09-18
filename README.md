# **Building CI/CD for API Project Proposal**

EC528

Panat Taranat, Yan Chen, Mella Liang, Peter Wang, Kaito Yamagishi

## 1. Vision and Goals of the Project:

Doubly is a URL shortener service that shortens URLs into easy to remember English phrases consisting of two words (one adjective followed by one noun). The key component of this project is the CI/CD pipeline that allows incremental changes to be developed, tested, verified and deployed in an automated manner. Following core DevOps principles will allow the project team to strive for continuous improvement with minimal downtime, and to respond quickly to customer feedback and insights. The service also provides access to an API that will allow users to request a short link on our domain.

Important goals include:

- (Almost) Fully automated setup and deployment. The entire process for a developer to make changes to the codebase should require as little manual interaction as possible. Same with someone who is looking to deploy the project with their own host.

- The design of the Doubly frontend interface must be polished, as well as the API documentation for the service. There must be an interactive interface that facilitates the usage, functionality, and further development of the project.

## 2. Users/Personas of the Project:

Non-expert user is an individual who found a cool link on the internet and wants to shorten it to share with their friend(s). The link may be used 10s of times.

Expert or commercial user is an entity that shortens a link to their brand or resource for the general public. This link may be used hundreds or thousands of times. They may also be experts in using the API to fit the service to their needs.

One example of a non-expert user is Sharon, a PhD researcher who found an interesting research article. Rather than sharing the DOI (Digital Object Identifier), she needs an easy to remember mnemonic link to share with her colleagues during a brown bag meeting. It improves the experience of content sharing and allows users to keep track of what they have shared.

One example of an expert commercial user is a small business that has social media presence as well as a blog on their own website. David runs a landscaping business with a strong Instagram presence. Using Doubly, David shares links to specific articles in his Instagram stories or posts that his audience can easily type up. The link will be clicked through frequently in proportion to David’s audience size and reach. Link management and analytics will provide him with insights about his target demographic and the effectiveness of his advertising platforms.

One example of an expert API user is Andy, a web developer working on his SaaS startup that allows users to write notes in the cloud. Andy wants to let his users be able to share links to specific notes or notebooks but the generated link system he currently has is ugly, long, and hard to remember (see notion.so). Andy reads our API documentation and forks our open source project to generate short, two word URLs for his service with his domain name. Andy’s version of the API is hosted on his own cloud provider that supports Docker images. Andy can contribute features and bug fixes back to the Doubly open source project, thanks to our CI/CD pipeline.

## 3. Scope and Features of the Project:

**In-Scope Features:**

- Given a valid URL, our service will generate a shorter and uniquely identifiable alias of it, consisting of two or more words. This will henceforth be referred as a *short link*

- When users access a short link, our service will redirect them to the original link in real time with minimal latencyShort links should be generated randomly and not predictable

- The service should have high availability, facilitated by CI/CD and DevOps principles

- Short links will expire after a default timespan

- Every commit or pull-request by a developer will go through CI/CD pipeline, must pass all tests before being deployed

- The short link must be easy to understand, pronounce, and spell, with no offensive words or combinations (accomplished by choosing a good dictionary)

  

**Out-of-Scope Features: (not delivered as part of MVP):**

- We may allow the creation of custom short link (choose words)
- We may provide in depth link analytics such as originating location or referrer (Email, SMS, Direct, 3rd-party websites)
- We may work on a Chrome extension or browser plugin. The only way to use our service is by navigating to our website or using our API
- We may allow users to specify a custom expiration time
- We may allow the creation of an account for link management, which includes the ability to: 
  - Organize all links created by this account
  - Edit the title of the short link (but not the generated two word back half)
  - Redirect the short link to a different URL
  - View the total clicks
- We may have bookmarklet to turn the current URL into a Doubly shortened URL (using our API), and save to clipboard (similar to Instapaper JS bookmarklet)

## 4. Solution Concept

This section provides a high-level outline of the solution.Global Architectural Structure Of the Project:This section provides a high-level architecture or a conceptual diagram showing the scope of the solution. If wireframes or visuals have already been done, this section could also be used to show how the intended solution will look. This section also provides a walkthrough explanation of the architectural structure.Design Implications and Discussion:This section discusses the implications and reasons of the design decisions made during the global architecture design.The system components of the architectural design is as follows:Python Flask backend for providing REST APIs that allow frontend to consumeReact front end for service’s user interfaceNginx load balancer, among client-application, application-database, application-cacheGitHub Actions for CI/CD pipelineUbuntu docker image for development environmentOpenShift on MOC for hosting[put diagram here]In the diagram, when developers make any changes in the code and the commits are pushed to GitHub, GitHub Actions triggers the CI workflow. It builds the project with the changed contents, runs integration and unit tests, and then provides results of the tests in the pull request. If the changes introduce errors, the developer can go back to debugging. If there are no errors from the tests, the change is ready to be reviewed by another team member. When the team member approves the changes, from here it is the CD workflow. The changes get reflected to the staging server, then if there are no problems here too, the changes will be deployed to the production server hosted on MOC using OpenShift. This server is running Nginx, load balancing the server’s resource availability and efficiency.The client is the website that allows users to interact with service. It sends API requests to the server. To shorten a link, the client sends a POST request containing the original URL to the server. The server runs an algorithm to shorten the link, stores data related to the link in the database, and sends back the shortened link. When a user enters a shortened link on a browser, a GET request is sent to the server, to send back the original link by searching in the database, which directs the user to the website. In this case, a browser is also a client in this diagram. A user is also allowed to delete the shortened link on the host website, or the server deletes the link once the expiration date is reached.Design decisions for the architecture were made with compatibility in mind. After consulting the possible choices for the architecture from our mentors and some of our friends, some of our team members researched and scanned through each documentation and reported back to the group. From there, we checked which element with which element is compatible, and made a decision. Difficulty of developing is another component we had in mind while making decisions for the architecture, we wanted to keep things simple so went with a simple Flask API on Python with some UI libraries we can potentially use for the frontend.

**5. Acceptance criteria**
Minimum Acceptance criteria is a cloud service that consists of a simple UI that communicates with URL shortener API to provide a shortened URL to the user. Stretch goals are:
- Provide user with link management, analytics, and account creation
- Allow user to create a custom short link
- Extend the service into a browser plugin or bookmarklet

## 6. Release Planning:

Release 1 (Deadline: Sept. 27, Demo: Oct. 1)
- Find dictionary library for shortened links
- Write algorithm that convert link to shortened form
- RESTful API code
  - Post route to convert URL to shortened link
  - Get route to access original URL via shortened link
  - Delete route to delete shortened link or expired data
  - Put route to change URL to different shortened link
- CI/CD pipeline
  - Make final decisions on technologies and implement them with code
- Back end testing on API codeTest each API route, write different test cases
- Decide on a NoSQL database (leaning toward MongoDB)

Release 2 (Deadline: Oct. 11, Demo: Oct. 15)
- Functional UI interface for core features
- Front end tests and additional back end testing

Release 3 (Deadline: Oct. 25, Demo: Oct. 29)
- Add cache for frequently used links + unit testing

Release 4 (Deadline: Nov. 8, Demo: Nov. 12)
- Attempt to add Out-of-Scope features + integration testing

Release 5 (Deadline: Nov. 29, Demo: Dec. 3)
- Ensure every part of project is functional, stable, and verified
