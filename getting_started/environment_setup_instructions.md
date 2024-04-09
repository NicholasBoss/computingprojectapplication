# Getting Started

## Installation

To get started with the project, you need to gain access to the tools you need to create and run the project.

### Prerequisites

Gain access to AWS Academy, and the AWS Instance.

The following website contains instructions of how to do this. Also, the following videos may help you set up your AWS account.

[Creating Your Virtual Machine](https://cse-byui.org)

A summary of the steps are as follows:

1. Accept the invitation from AWS Academy from your email.

2. If you don't have an AWS account, create one. Be sure to set a DIFFERENT password than your BYU-I password.
AWS Academy is a different system than our BYU-I Canvas system.

You should be taken into the course you were invited to. If you land on the AWS Academy home page, click on the course you were invited to.

3. Click on `Modules` on the left side of the screen.

4. Click on the `Launch AWS Learner Lab` link.

5. Click on the `Start Lab` button.

6. Click on the `AWS` button when the red circle turns green.

You should now be in the AWS console. You can now start the process of setting up your virtual machine.

1. Up on the top of the screen, click the box with `N. Virginia` in it. Change the region to `Oregon`.

2. Click on the `Services` drop down menu and type `EC2` in the search bar. Click on the `EC2` link.

3. Click on the `Instances` link on the left side of the screen.

4. Click on the cloudshell icon which is the first icon to the right of the search bar.

5. Paste the following commands into the terminal and run them one at a time to install the tools you need to run the project.

```
git clone https://github.com/byui-bwh/db-workstation-automation.git
```

```
cd db-workstation-automation
```

```
cat provision_vm.sh
```

```
. ./provision_vm.sh
```

6. The script will ask you for your numbered BYU-I email address. Enter it and press enter.

The script will configure and setup your virtual machine. This process may take a few minutes.

Once the script is finished, it will provide you with a URL to access the virtual machine. Wait about a minute then copy and paste the URL into your browser.

The URL will take you to the login page for the virtual machine. The password is `Cit325password123!`.  
After you get past the DCV client login, you will be taken to the online Ubuntu instance.  
You will see a student user account. Click on it and enter the password again.  
The first time you login, the system will seem to freeze. DO NOT REFRESH OR CLOSE THE PAGE. The system is setting up your account.  
It will automatically refresh and prompt you to enter the password again. This time, it will prompt you to enter the password one final time, and then you will be asked to change it. Make sure it is at least 8 characters long with at least one number and one special character. Do not forget this password.

Here is a playlist that will help you get started with the AWS Academy environment:  
[Videos](https://youtube.com/playlist?list=PLH00JS9rvd3ERkGsmA36xFIgFfHxGDzDH&si=uUa16XU3eqm4zK5m)

### Setting up GitHub

The virtual machine is an Ubuntu instance that you can use to run the project. You can access the virtual machine by going to the URL provided by the script.

We will be using VS code and GitHub to create and manage the project. If you do not have a GitHub account, please make one with your numbered BYU-I email. You can use the following link to create an account. **You do not need one as of today, but you will need one in the future.**

[GitHub](https://github.com)

We will also be using GitHub Desktop to manage our GitHub repositories. 

If you are unfamiliar with GitHub Desktop, here are some instructions to help you get started.

1. Open GitHub Desktop and sign in with your GitHub account.

2. Once you've signed in, leave the default settings for the email and click continue.

We want to create a repository on the desktop for all our files that we want to have access to outside the instance or as a backup for your files on your local machine.

3. Click on the `Create Repository on Local Hard Drive` option, name it, and designate the location as the Desktop. For all files you want to have access to outside the instance, place them in this folder.

4. Click the `Create Repository` button.

5. Now we need to create a repository on GitHub. Click on the `Publish Repository` button.

6. Name the repository and add a description if you'd like. Make sure the repository is private and click the `Publish Repository` button.

7. Any files you want to have access to outside the instance, copy them to the repo folder on the desktop. Open GitHub Desktop and click on the `Changes` tab. You should see the files you copied to the repo folder.

8. Add a summary of the changes in the `Summary` box and click the `Commit to main` button.

9. Click the `Push origin` button to push the files to the GitHub repository.

In the repo you created on the instance, open it with VS Code. You can then create the files that are needed for the project. Once you have created the files, you can push them to the GitHub repository.

### Setting up VS Code

We will be using VS Code to create and manage the project. This is provided in the instance and is already configured.

To open VS Code, click on the icon on the left of the screen.

### Setting up the Project

In our "Teams"/"Slack"/"Discord" channel, you will find a link to the step by step instructions for the project. You can use these instructions to create the files needed for the project.

