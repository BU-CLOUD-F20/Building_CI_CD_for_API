#### **Reason for Automatic CI/CD pipeline**

Manually deploying a pipeline or application on AWS (or any cloud provider) is both difficult and tedious because of server setup, configuration of pipeline, provision integration among all components.



#### **Competitors**

- [One Click Automation Solution](https://blog.insightdatascience.com/one-click-automation-bbf95b15980a)

  - Use a set of existing pipeline to streamline automatic CI and CD
    - Hashicorp’s Terraform
      - Write Infrastructure as Code
      - Manage Configuration Files in VCS (version control system)
      - Automate Provisioning
        - Trigger a plan when changes pushed to repo (similar to GitHub Actions)
      - Good AWS integration
        - Provisions infrastructure on AWS
    - Hashicorp’s Packer
      - Open source tool for creating identical machine image for multiple platforms from one configuration
      - Very similar to a Docker image
    - Shell Script
      - Script written to build all Packer AMIs (Amazon Machine Image) and run Terraform for deployment on AWS

- [VULTR](https://www.vultr.com/features/one-click-apps/)

  - Platform to deploy pre-configured applications and game servers with single click
    - Support for Docker, GitLab
  - Not free!

- [Heroku CI and CD](https://www.heroku.com/continuous-delivery)

  - Heroku Pipelines
    - Organize apps with same codebase into deployment pipelines with UI
    - Easily promoted from one stage to next
  - Heroku CI
    - Auto run tests on every push to GitHub
  - Review Apps
    - Spin up a test app for review
  - GitHub Integration
    - Automatic or manual deployment of branches

- Atlassian’s [Bamboo](https://www.atlassian.com/software/bamboo)

  - Trigger to build code on commit
  - Run automated tests with UI to see test coverage
  - Deploy after build
  - Offers trial plans to start for free, paid later

- [Jenkins](https://www.jenkins.io/)

  - CI/CD
  - Runs on most popular OS
  - Support for plugins

  

#### **AWS Competitors**

- **AWS’s own services-**
  - AWS CodePipeline
  - Pricing:
  - Monthly charges will vary on your configuration and usage of each product, but if you follow the step-by-step instructions in this guide and accept the default configurations, you can expect to be billed around $15 per month

- **CircleCI** 

  - What do they do?

    - Listen for changes in Github/Bitbucket repo

    - Config.yml file in the root on the repo

      - Define a Docker image

      - Define jobs eg: checkout.

      - Cache previous build to save download time

      - Run

      - Save cache

      - Workflow (specify each branch…)

        ![img](https://lh6.googleusercontent.com/r1ashK2moxnShNySvcvLH07VnSE_g1CokXJLSBPoHgoyjbMz2ajCPfJ4F_IVO5AJa-MmnI-p9gSNcs51OTN9mJHvzcGUG2V_4VhXFcMljFHxGPDMRJohGcAWm5PB0o7YZM49Mg72)

    - Do stuff

      - Deploy
        - They only download changed File
        - Auto-create a readme file looks like![img](https://lh3.googleusercontent.com/XHcJ32X8mrkxlSWR4q_3D0Cs_MmOGT0HXO2l4-hp8GVlm5dvg0D9ysu6A4gUWeJTKxC7Yuuoq0t0wuPmP-bxnqEIAc4WnP_EDp0fSvHpl98LhzcYxPEOitSCN2dKZJK_V9_He-Ct)
      - Setup environment
      - Download dependencies
      - Compile static assets
      - Refactor to code standards

    - Deploy to AWS using AWS CodeDepoly

      - Config by another .yml file

    - Slack auto notification when a deployment happens

    - Pricing:![img](https://lh5.googleusercontent.com/WLTibd6FNLPAZ0m4jE1gzN4focIlLejMzHEqrO2AIdOHZBitvrkJ_Lu6UL8r8Mr_sse_UVXT9fSMAGQ3T7pArtWsx0Bxadr53RsUu9a6Yt9gvvwG4A380UshHB8TFXG7f3PqEKpe)

- **DIY AWS pipeline**

  - [Using AWS CodeDeploy](https://www.youtube.com/watch?v=zkNdHv1iMgY)



#### Conclusion

These competitors show various ways to improve CI/CD workflow. Some common flows are comprehensive user console, auto run testing, auto deployment and much more. By learning from them, we choose to also include auto testing and deployment into our product. However, a lot of these competitors’ services have limitations such as not being open source, not free, limited options and high learning curve. While having similar features in our pipelines, we will also pay close attention to user stories. For instance, since most developers are tied to the GitHub ecosystem, we choose to use Github actions for our CI to minimize the user learning curve. Moreover, our product is open source, free to use, and can be self-hosted. 





