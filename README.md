# **Building CI/CD for API Project Proposal**

###### EC528 Fall 2020

###### Team Members: Panat Taranat, Yan Chen, Mella Liang, Peter Wang, Kaito Yamagishi
###### Mentors: James Colley, Surya Jayanthi, Ata Turk


====

This project is about the design and development of a CI/CD pipeline setup tool that can be used for web API development and deployment on OpenShift. This repository contains the example application of a URL shorterner that we used to test the pipeline. The pipeline setup tool is at https://github.com/yanchen01/cicd-cli

# Requirements

* Repository on GitHub where API development will take place
* GitHub personal access token with repo level access ([instructions here](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token))
* OpenShift instance with server URL and login token

*If building pipeline tool from source*

* Node.JS

# How to use the pipeline setup tool 

## Option 1: Build from Source

1. Clone [pipeline setup tool repo](https://github.com/yanchen01/cicd-cli) and build the tool (requires Node and npm).
2. `npm install` to build the application
3. `npm link` to add the tool to your $PATH

## Option 2: Release binary

1. Download the precompiled binary for your operating system from the [Releases page](https://github.com/yanchen01/cicd-cli/releases)
2. Add the program to the path or copy it into your API's repository (you might want to add to `.gitignore`)

## Usage

1. `cicd setup`
	* Sets up necessary workflow files (Refer to Workflow Files section below)
2. `cicd config`
	* Configure repo name, access tokens, deployment targets
3. Commit and push the workflow files to your repo
4. The pipeline is ready
5. Edit code on a feature branch
6. Make a pull request into master
7. Pipeline workflows will trigger and run tests
8. Manually approve the pull request
9. Pipeline will deploy to OpenShift if all tests passed

# Run the URL Shortener App Locally

1. Install virtual env on your local machine
    1. Windows User: python -m venv env
    2. Mac User: python3 -m venv env
2. Enable virtual env
    1. Windows User: source venv_pc
    2. Mac User: source venv_unix
3. Install dependencies
    1. Windows User: pip install -r requirements.txt
    2. Mac User: pip3 install -r requirements.txt
4. Run Flask App
    1. Windows User: python app.py
    2. Mac User: python3 app.py
5. OR run Flask App via Docker Container (docker installed)
    1. docker build -t flaskapp:latest .
    2. docker run -it -p 5000:5000 flaskapp
    3. Optional: docker run -it -d -p 5000:5000 flaskapp (automatically runs in background)
6.  Flask app runs on http://localhost:5000/

# Workflow Files (.github/workflows/)

Any of these workflows files/jobs can be manipulated for personalization. Check out more about editing the workflow files here:

https://docs.github.com/en/free-pro-team@latest/actions/reference/workflow-syntax-for-github-actions

The GitHub actions marketplace has bunch of third party GitHub actions you can add to your workflows:

https://github.com/marketplace?type=actions



1. ci.yml (Triggers on any pull_request)

   1. Formatting (User choice of autoyapf PEP-8 style or Black style)
      1. Changes are automatically pushed to the current branch

   2. Unit Test (PyTest)
      1. Fails if test coverage is under 90%

   3. Test Deploy to OpenShift
      1. Creates a build config of the name of the current branch

         ​	Any necessary integration tests such as Selenium on the OpenShift pipeline should occur here

   4. Wait for One Hour for Integration Tests on OpenShift
      1. Pauses for one hour before deleting the testing environment. Run tests on OpenShift during this action

   4. Cleaning up OpenShift
      1. Deletes any config, builds and pods related to the test deploy in step 3


   2. cd.yml (Triggers on push to the master branch)

      1. Deploying Production to OpenShift
         1. If a build with the name of the repository exists, roll out the changes to that build
         2. Else, create a build config with the name of the repository and deploy the master branch to OpenShift

# Videos and Slides

* [Final Project Video](https://drive.google.com/file/d/156mp9SgMFp6GuxUjJB9t4ZjiQ9Me95_x/view?usp=sharing) and [Slides](https://docs.google.com/presentation/d/10TDFWE4x0daBH89_soXN2L1T9xW4o7x9zHawPGI-0jg/edit?usp=sharing)
* [Project Poster](https://docs.google.com/presentation/d/1I2vLbIJFdigatx3YsvwHhidczOAy0O72gUNoas7e8LE/edit?usp=sharing)
* [Sprint 5 Video](https://drive.google.com/file/d/1b5u_TCzTKjQPCLFwBsIUrurld_uDhqV0/view?usp=sharing) and [Slides](https://docs.google.com/presentation/d/1W0ZxpGOTdOr8Iw1tBM92GzvbQd87qZupM1jeMjfjScg/edit?usp=sharing)
* [Sprint 4 Slides](https://docs.google.com/presentation/d/1DTBL3iiL89ZFYMjmdpY9vEH-vXr6Yf1MTqE4xwlGMd0/edit?usp=sharing)
* [Sprint 3 Slides](https://docs.google.com/presentation/d/1EOoE3-8W3tEjHZigkjZXEqBkYvAc8JTZLaWJyUksesQ/edit?usp=sharing)
* [Sprint 2 Slides](https://docs.google.com/presentation/d/1JLhh-rAteCQgUn7dJXz_MAQW1wK7uLARXMfLAjHoWUE/edit?usp=sharing)
* [Edge Computing Presentation](https://docs.google.com/presentation/d/1gHzR5pzkT7up5B-OAuBLnUcTEA74QiI7eBkth8NwtjU/edit?usp=sharing)

# Documentation

* **[Project Description](/Documents/project_description.md)** The original proposal by the mentors
* **[Proposal](/Documents/proposal.md)** Our project proposal with preliminary architecture overviews
* **[Competitor Research](/Documents/research.md)**
