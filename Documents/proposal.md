# **Building CI/CD for API Project Proposal**

###### EC528

###### Team Members: Panat Taranat, Yan Chen, Mella Liang, Peter Wang, Kaito Yamagishi
###### Mentors: James Colley, Surya Jayanthi, Ata Turk



## 1. Vision and Goals of the Project:

We are working on a CI/CD pipeline that can be used for API development. We will use an example of a URL shortener API as a demonstration of our pipeline, though pipeline will work with most Python APIs. The pipeline will allow incremental changes to be developed, tested, verified, and deployed in an automated manner. Following core DevOps principles will allow the project team to strive for continuous improvement with minimal downtime, and to respond quickly to customer feedback and insights.

Important goals include:

* (Almost) Fully automated setup and deployment. The entire process for a developer to make changes to the codebase should require as little manual interaction as possible. Same with someone who is looking to use our repo as a GitHub template for their own project.
* The URL shortener API will be served on an attractive interface
* Unit tests can be written and integrated into the pipeline on GitHub
* Integration tests will be performed on OpenShift
* From the first deployment, the API and pipeline will have high availability


## 2. Users/Personas of the Project:
Andy is a user of the CI/CD pipeline with an existing project. Andy already has a simple Flask webapp on a GitHub repo. Andy has written some unit tests and wants to deploy his app onto Openshift. He reads the documentation for our CI/CD pipeline, grabs the CLI tool from npm, and uses our CLI tool to quickly setup GitHub Actions workflows. Now, whenever Andy makes commits to this repo, the code will go through unit tests and integration tests. If the tests have passed, the code will be deployed on OpenShift, serving users of his webapp with the latest version.

Brian is a user starting from scratch. Brian can grab our CLI tool from npm. The tool will guide him through the process of setting up and deploying his webapp. As he develops, he can add tests and the tool can regenerate the workflow yaml files as needed. This allows Brian to perform test driven development on the cloud as early as possible.

## 3. Scope and Features of the Project:

**In-Scope Features**

* Allow adding and running of unit tests in CI
* Easy installation and configuration of the pipeline, can be customized to different projects
* Extensible in functionality, by allowing users to embed unit tests or API integration tests
* The API being developed should have high availability, a failed test should not bring down the service
* Every commit or pull-request by a developer will go through CI/CD pipeline, must pass all tests before being deployed
* Failed builds and tests will alert developers
* Ensure the security of secrets and sensitive data/tokens in the pipeline

**Out-of-Scope Features (not delivered as part of MVP)**

* Backwards compatibility with Jenkins
* Dashboard interface for developers to see problems and status of CI/CD pipeline
* The URL shortener API is a demonstration, so extensive development or design of the shortener API is not in scope
* Can be customized to host other than OpenShift, like Kubernetes


## 4. Solution Concept

The system components of the architectural design is as follows:
* GitHub Actions for unit testing and deployment
* CLI tool for setting up GitHub Actions workflow yaml files and viewing logs
* OpenShit Actions to deploy from GitHub
* Docker for containerizing web app
* OpenShift on MOC for hosting production app and testing environment (integration, load/stress)

Majority of our code will be in the CLI tool for generating GitHub Action workflow files.  
Development of the CLI tool is being done at https://github.com/yanchen01/cicd-cli


<img src="/assets/diagram.png">

In the diagram, when developers make any changes in the code and the commits are pushed to GitHub, GitHub Actions triggers the CI workflow. It builds the project with the changed contents, formats code, runs unit tests with pytest, and then provides results of the tests in the pull request.  

If the changes introduce errors, the developer can go back to debugging. If there are no errors from the tests, it is deployed to OpenShift for integration testing. Once it passes integration testing, check marks will appear on the GitHub Actions page.

The change is ready to be reviewed by another team member as a pull request. When the team member approves the changes, the code will be deployed to the production server hosted on MOC using OpenShift.

We will be developing unit tests and end-to-end API integration tests alongside the development of the URL shortener. These tests will allow us to verify the proper function of various system components, such as backend and frontend.

Design decisions for the architecture were made with usability and ease of development in mind. We compared the features of GitHub Actions to Jenkins and found the following:

**GH Actions**

* Better community support and bigger extension marketplace than Jenkins
* Uses common scripting languages, JS and bash
* Infrastructure as Code, our workflow defines the process
* Built-in integration with GitHub, useful for many open source projects

**Jenkins**
* Very mature, over 9 years old, with lots of documentation and answered questions
* Highly extensible, but some plugins are poorly maintained or has conflicts
* Uses master/node relationships
* Need to learn Groovy script (Java-like syntax)
* High support overhead, we will need at least one person dedicated to Jenkins always

We assume that many developers of open source projects are familiar with the GitHub ecosystem, so using GitHub Actions, Packages, and Templates will increase our reach as well as ease-of-use. GH Actions also has built-in integrations with common deployment targets, like AWS, Azure, Heroku, and Google Cloud.

## 5. Acceptance Criteria

Minimum acceptance criteria is a CI/CD pipeline for an API developed and tested with our example URL shortener API. It will detect all commits and pull requests in a GitHub repository, and run the pipeline defined by our GitHub actions configurations. This will build a docker image, run tests, and deploy the changes to a running production server with no stoppage.

* Push to production is one-click, fully automated
* Any code that does not build or passes tests will not make it to production
* Generic and extensible, can be easily implemented by an API developer using Flask/Python


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
  - Set up a GitHub actions workflow that will detect a push (source) then cause some action
  - Explore added options on the yaml file
  - Explore tests: write tests on PyTest, implement on GitHub actions and successfully accept/reject new pushes to the repository
- Back end testing on API codeTest each API route, write different test cases
- Decide on a NoSQL database (leaning toward MongoDB)
- Tests may include:
  - Formatting using pep8
  - Token-based authentication
  - Test short link generation
  - Test API routes
- Decide on a NoSQL database (leaning toward MongoDB)

Release 2 (Deadline: Oct. 11, Demo: Oct. 15)
- Functional UI interface for core features
- Unit tests for front end and back end
- CI/CD pipeline
  - Create build stage that creates a docker container with the contents that was updated
  - Make sure the source is getting past the build stage
  - Work on deploy stages
    - First host on the staging server, then after final confirmation deploy to production
- At this point, core features of the API and the CI/CD pipeline should be functional and highly available


Release 3 (Deadline: Oct. 25, Demo: Oct. 29)
- This release will focus on tuning performance and testing
- Add cache for frequently used links + unit testing
- CI/CD pipeline
  - Work on test stage; write, debug and run the test files
  - Implement smoke, unit and integration testing

Release 4 (Deadline: Nov. 8, Demo: Nov. 12)
[Sprint 4 Demo Slides](https://docs.google.com/presentation/d/1DTBL3iiL89ZFYMjmdpY9vEH-vXr6Yf1MTqE4xwlGMd0/edit?usp=sharing)
- Attempt to add Out-of-Scope features + integration testing
- CI/CD pipeline
  - Explore the extensibility and application of our pipeline to other projects
  - Work on areas that need improvement for better usability

Release 5 (Deadline: Nov. 29, Demo: Dec. 3)
- Ensure every part of project is functional, stable, and verified
- Check current state of product with MVP, acceptance criteria
- Complete documentation on how to use our pipeline in other projects
