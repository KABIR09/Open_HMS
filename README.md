# Group-G


DOCUMENTATION


**INSTALLATION**

    1. Make sure that the target environment for the project has Python 3.8.
    2. Clone the git repository at the desired destination.
    3. Once that is done, open a command prompt window (Windows) or a Terminal window (Mac OS & Linux).
    4. Install the Requirements: pip install -r requirements.txt.
    5. Navigate to the folder where the application was opened and traverse deeper through the directory until you are in the same directory that contains the file called manage.py.
    6. Then,make database migrations: “python manage.py makemigrations” followed by “python manage.py migrate”
    7. Type in the command "python manage.py runserver" on your command prompt or Terminal window and run it.
    8. Take the HTTP address from the line beginning with "Starting development server at...".Put that web address into a web browser of your choice and go to it. The URL you enter should look something like this: http://127.0.0.1:8000
    9. You now have the Open_HMS application running.
    


**LOGINS AND PASSWORDS**

To sign into Open_HMS as an , you can use the following credentials:

Some of the sample credentials for Doctor are:

Username: amit

Password: 123

Some of the sample credentials for Patient are:

Username: rohan

Password: 123



**STEPS FOR DEPLOYMENT:**

 This workflow will build and push a new container image to Amazon ECR, and then will deploy a new task definition to Amazon ECS, when there is a push to the main branch.
 
    1. A dockerfile is created containing the commands to setup and deploy the instances.
    2. An AWS ECR is cretaed, which is a container image repository used to store the docker images that are created for every deployment.
    3. AWS ECS is a cluster service that is used to deploy the docker image from ECR to a fargate server. The server task defination is available in deploy.json.
    4. A github action file is created to integrate and deploy for every push to the github repository which perform the following task to implement CI/CD
    
    Features:-
    
        ◦ Setup: creating OS, virtual environment and github tokens.
        ◦ Checkout: Initializing Repository,deleting contents,disabling automatic garbage collections.
        ◦ Configure AWS credentials: Configure with your AWS credentials
        ◦ Login to amazin ECR: Uploads docker image to the ECR repository.
        ◦ Build,tag and push image to amazon ECR:Build a docker container and sending build context to docker daemon.
        ◦ Fill in the new image ID in the Amazon ECS task definition:
        ◦ Deploy Amazon ECS task definition: Here,Deployment is started.
        ◦ Post Login to Amazon ECR: Post job cleanup
        ◦ Post configure AWS credentials: Post job cleanup
        ◦ Post checkout: Post job cleanup
        ◦ Complete Job: Cleaning up orphan processes
        
**Project Overview:**

**About Open_HMS:**

In our Open_HMS Project focuses mainly on dealing with the hospital records.WeCare Management System will help doctors to create their personal accounts.Here,Multiple Doctors can register on the website with their details and Multiple patients can take appointment for a specific doctor.Here Doctor can create prescription by adding,updating or deleting medicines on the day he wants.All this will be maintained and stored in the system.

**Doctor Dashboard:**

Our WeCare Management System have the feature of Signup and Login where a Doctor who have visited our site can register themselves by providing their Name, unique username, Mobile number, Department and their address.

  Registered Doctor’s can see their details like profile picture and name.He can also see the number of patient that are under his observation and his own department.
  
  Doctor can see the patient’s details that are under him by just searching with the help of the patiemt ID.
  
  Doctor can add prescription for every patient and can also view the older prescriptions history of the patient.He can also Create,Update nad Delete multiple medicines in the prescription.                            
  
  
**Patient Dashboard:**

Same as Doctor’s Dashboard Feature,here Patient can also register themselves by providing their basic details like name,username,mobile number and addresss and can choose the doctor name & department to whom they want to visit.
      
  Patient can see the details of the doctor to whom he is referred to like doctor contact number and the department of the doctor along with the symptoms of the patient.Patient can also update their summary.
  
  Under Patient summary section, patient can see his/her details and doctor he/she is referred to along with details that were taken during his registration like Disease and Symptoms, Allergy, Immunization taken or not, is there any history of illness and the diagnostic results.
  
  Patient dashboard,Patient can see the doctor whom he is referred to,his necessary contact details  patient can  see all prescriptions along with previous prescription that are prescribed in which details include Date, Medication Item, Frequency, Dose, Dose unit, Direction Duration, Form, Additional Instructions and Substance.

