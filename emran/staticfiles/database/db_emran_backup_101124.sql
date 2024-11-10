PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'emran','0001_initial','2024-11-10 08:19:15.132277');
CREATE TABLE IF NOT EXISTS "emran_certificationscoursestrainings" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "cct_name" varchar(300) NOT NULL, "cct_description" text NULL, "cct_type" varchar(51) NOT NULL, "cct_offering_organisation" varchar(300) NOT NULL, "cct_funding_organisation" varchar(300) NULL, "cct_key_information" text NULL, "cct_hasexpire" bool NOT NULL, "cct_serial_no" varchar(10) NULL, "cct_start_date" date NOT NULL, "cct_end_date" date NULL, "cct_image" varchar(500) NULL, "cct_online_credential" varchar(1000) NULL);
INSERT INTO emran_certificationscoursestrainings VALUES(1,'Introduction to Tensorflow and Keras',replace(replace('This Introduction to TensorFlow and Keras course will enrich your knowledge about all the essential Python libraries and guide you to install them step by step. It will start by explaining what TensorFlow is and its various functionalities. It will then take you to get a brief understanding of the prerequisites to understand tensors before moving on to the installation chapter. Once your concept of TensorFlow is clear, the course will have you navigate through Neural Networks and discuss how you can write Tensor code to perform distinct operations. Before wrapping up the course, you will also learn about the newer version (TensorFlow 2.x) and learn to perform Linear Regression using TensorFlow. In the last phase, the course will take you through the hands-on session, which will discuss two use cases and finally throw light on what Keras is, its features, character recognition, and image classification using CNN.\r\n\r\nhttps://www.mygreatlearning.com/academy/learn-for-free/courses/introduction-to-tensorflow-and-keras','\r',char(13)),'\n',char(10)),'all,course','Great Learning Academy',NULL,replace(replace('- Great Learning Academy - Free course\r\n- Deep learning fundamentals; Libraries: Tensorflow, Keras\r\n- Implementation with Keras and TensorFlow separately\r\n- Section-wise test','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-01',NULL,'emran/staticfiles/myresources/courseandcertificate/glearn-intro2TFandKeras.jpg','https://www.mygreatlearning.com/certificate/XSVNGIBX');
INSERT INTO emran_certificationscoursestrainings VALUES(2,'Introduction to Deep Learning',replace(replace('This online Introduction to Deep Learning course aims to familiarize learners with all the crucial  deep learning concepts currently being utilized to solve real-world problems. You will learn about the history and applications of Deep Learning and understand the role of the second wave in DL. Also, comprehend how ML differs from DL, go through the essential terms in Deep Learning called artificial neural networks, and comprehend the Deep Learning fundamentals.\r\n\r\nYou will also go through the demo on Tensorflow Playground, CNN, and neural networks. Learn about the involvement of a basic set of layers in DL and learn about activation function and CNN. Gain knowledge regarding RNN, LSTM, types of chatbots, and conventional interfaces. Dig deeper into the concept of Deep Neural Networks and go through concepts like boolean gates, artificial neurons, Rosenblatt Neuron Perceptron, and artificial neural networks and their mechanism in detail with relevant demo and code examples.\r\n\r\nEager to dive deeper into the Machine Learning field? Great Learning offers Best Artificial Intelligence and Machine Learning Courses that are highly valued by our learners. Enroll in the program of your interest and earn a certificate of course completion that validates your industrial skills.\r\n\r\nhttps://www.mygreatlearning.com/academy/learn-for-free/courses/introduction-to-deep-learning-1','\r',char(13)),'\n',char(10)),'all,course','Great Learning Academy',NULL,replace(replace('- Great Learning Academy - Free course\r\n- Deep learning fundamentals\r\n- ANN, CNN, convolution, pooling, softmax, learning. loss, back-propagation\r\n- Section-wise test','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-01',NULL,'emran/staticfiles/myresources/courseandcertificate/glearn-intro2DL.jpg','https://www.mygreatlearning.com/certificate/MFLMYZNY');
INSERT INTO emran_certificationscoursestrainings VALUES(3,'Machine Learning Algorithms',replace(replace('This online Machine Learning Algorithms course has been designed keeping in mind that a novice learner should be able to grasp the concepts and understand algorithms with examples. This course covers the introduction to Machine Learning and the basics of algorithms, along with a theoretical and practical understanding of supervised, unsupervised, and reinforcement learning. You will also gain skills to employ K-nearest Neighbor, Naive Bayes and Random Forest algorithms, and Linear Regression and Support Vector Machines (SVM) techniques to accomplish Machine Learning tasks. A tonne of practical Python demonstrations are offered to comprehend the concepts better. \r\n\r\n\r\nhttps://www.mygreatlearning.com/academy/learn-for-free/courses/machine-learning-algorithms','\r',char(13)),'\n',char(10)),'all,course','Great Learning Academy',NULL,replace(replace('- Great Learning Academy - Free course\r\n- Machine learning models\r\n- Classification, regression, clustering\r\n- Section-wise test','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-01',NULL,'emran/staticfiles/myresources/courseandcertificate/glearn-MLalgo.jpg','https://www.mygreatlearning.com/certificate/DEJNIEJZ');
INSERT INTO emran_certificationscoursestrainings VALUES(4,'Python for Machine Learning',replace(replace('The Python Programming for Machine Learning course shall focus on the elements and features available in Python programming for Machine Learning tasks, along with a few demonstrated samples. It shall begin with introducing you to the NumPy library and continue with helping you understand its arrays, intersection, differences, loading, and saving as you follow the first half of the course. The second part engages you by covering Pandas library and its objects, data frames, and functions. Take the quiz at the end of the course to test your skills and evaluate your gains to secure your free certificate. \r\n\r\n\r\nhttps://www.mygreatlearning.com/academy/learn-for-free/courses/python-for-machine-learning3','\r',char(13)),'\n',char(10)),'all','Great Learning Academy',NULL,replace(replace('- Great Learning Academy - Free course\r\n- Machine learning concepts: Data cleaning, splitting, validation; Concepts of ML models; Result evaluation, scoring\r\n- Python, Numpy, Pandas, Scikit-learn\r\n- Section-wise test','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-01',NULL,'emran/staticfiles/myresources/courseandcertificate/glearn-py4ML.jpg','https://www.mygreatlearning.com/certificate/MEQIVGAB');
INSERT INTO emran_certificationscoursestrainings VALUES(5,'Datascience Foundation',replace(replace('The Data Science Foundations course proffers your knowledge on the introduction to the subject and gives you insights into the different phases of its life cycle. The course covers topics about various tasks carried out in Data Science and different programming languages that are compatible to work with to accommodate the tasks efficiently, and Machine Learning, contributing to the dynamic behavior of machines and making significant associations with DS. The analytics landscape is another significant component within an organization, which you will learn in the latter part of the course, to understand workflow and asset distribution thoroughly. You will have to take an assessment to test your gain on the subject. The course also provides you with study materials for your reference at any given point after enrolling in it. \r\n\r\n\r\nhttps://www.mygreatlearning.com/academy/learn-for-free/courses/data-science-foundations','\r',char(13)),'\n',char(10)),'all,course','Great Learning Academy',NULL,replace(replace('- Great Learning Academy - Free course\r\n- Data science concepts\r\n- Python, Numpy, Pandas\r\n- Section-wise test','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-01',NULL,'emran/staticfiles/myresources/courseandcertificate/glearn-datSciFound.jpg','https://www.mygreatlearning.com/certificate/VOJHGZGI');
INSERT INTO emran_certificationscoursestrainings VALUES(6,'Data Visualisation with Python','','all,training','Intersect Australia','Deakin University',replace(replace('- Intersect Australia & Deakin University collaborative training program\r\n- 3 hours\r\n- Python, Matplotlib, Seaborn, Fundamental and advanced graphs/plots','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-01',NULL,'emran/staticfiles/myresources/courseandcertificate/intersect-datVisPy.jpg',NULL);
INSERT INTO emran_certificationscoursestrainings VALUES(7,'Data Manipulation with Pytho','','all,training','Intersect Australia','Deakin University',replace(replace('- Intersect Australia & Deakin University collaborative training \r\n- 3 hours\r\n- Python, Numpy, Pandas','\r',char(13)),'\n',char(10)),0,NULL,'2022-03-01',NULL,'emran/staticfiles/myresources/courseandcertificate/intersect-dataManPy.jpg',NULL);
INSERT INTO emran_certificationscoursestrainings VALUES(8,'Google Cloud Fundamentals: Core Intrastructures','','all,training','AppsBroker Academy',NULL,replace(replace('- 5-hour dedicated session\r\n- Google Cloud Fundamentals\r\n- Google Cloud Infrastructures\r\n- Google Cloud IaaS\r\n- Part-wise lab and test','\r',char(13)),'\n',char(10)),0,NULL,'2022-04-25',NULL,'emran/staticfiles/myresources/courseandcertificate/gCloudFund-ConInfra.jpg',NULL);
INSERT INTO emran_certificationscoursestrainings VALUES(9,'IEEE EMBS - Summer Camp 2022','Institute of Electrical and Electronics Engineers (IEEE) Engineering in Medicine and Biology SocietyEMBS - Summer Camp 2022','all,bootcamp','IEEE EMBS - Summer Camp 2022',NULL,replace(replace('- IEEE EMBS - Summer Camp 2022\r\n- EMBS Students Activities Committee\r\n- 8 days, 24 hours\r\n- Recent and trending research\r\n- Healthcare, Sports, and Production industries related research','\r',char(13)),'\n',char(10)),0,NULL,'2022-10-05',NULL,'emran/staticfiles/myresources/courseandcertificate/ieeeembs-summschl2022.jpg',NULL);
INSERT INTO emran_certificationscoursestrainings VALUES(10,'g·tec - BCI & Neurotechnology Spring School 2022','g·tec, an Austria-based BCI hardware and software research and development company organised a 10-day long conference. It allows to let the researcher know what is going on in recent industry innovations.','all,conference,bootcamp','g·tec',NULL,replace(replace('- g·tec Neurotechnology Spring School 2022\r\n- 10 days, 130 hours, 12 credits\r\n- Academic and industrial topics\r\n- Healthcare, Games, VR, Sports, Entertainment, Production, Education & Research Industries','\r',char(13)),'\n',char(10)),0,NULL,'2022-05-20',NULL,'emran/staticfiles/myresources/courseandcertificate/gtec-neurotechSprSchool2022.jpg',NULL);
INSERT INTO emran_certificationscoursestrainings VALUES(11,'Intermediate Machine Learning',replace(replace('Intermediate Machine Learning\r\nHandle missing values, non-numeric values, data leakage, and more.\r\n\r\nhttps://www.kaggle.com/learn/intermediate-machine-learning','\r',char(13)),'\n',char(10)),'all,course','Kaggle',NULL,replace(replace('- Offered by Kaggle\r\n- 14 hours, 7 Lessons\r\n- Lessons + hands on practice test\r\n- Intermediate level knowledge of ML: data preparation, cross validation, XGBoost, data leackage','\r',char(13)),'\n',char(10)),0,NULL,'2024-07-05',NULL,'emran/staticfiles/myresources/courseandcertificate/kaggle-int-ml.png','https://www.kaggle.com/learn/certification/wwmemran/intermediate-machine-learning');
CREATE TABLE IF NOT EXISTS "emran_honorsandawards" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "haw_title" varchar(300) NOT NULL, "haw_issuer_organisation" varchar(300) NOT NULL, "haw_associated_organisation" varchar(300) NULL, "haw_start_date" date NOT NULL, "haw_short_description" varchar(300) NOT NULL, "haw_description" text NULL);
INSERT INTO emran_honorsandawards VALUES(1,'InUPC Champion','Hajee Mohammad Danesh University of Science and Technology University (HSTU), Dinajpur-5200, Bangladesh','Hajee Mohammad Danesh University of Science and Technology University (HSTU), Dinajpur-5200, Bangladesh','2009-02-16','Intra-University Programming Contest (InUPC) Champion - HSTU, Bangladesh · Feb 2009',replace(replace('As a champion team member, I received a championship certificate and prize in, HSTU Intra-University Programming Contest (InUPC), an event arranged at HSTU IT Fest-2009. \r\nI participated as a participant of a team with 3 members, during the Bachelor of Science (B.Sc) in Computer Science and Engineering program at HSTU.','\r',char(13)),'\n',char(10)));
INSERT INTO emran_honorsandawards VALUES(2,'Undergraduate Department Topper','Hajee Mohammad Danesh University of Science and Technology University (HSTU), Dinajpur-5200, Bangladesh','Hajee Mohammad Danesh University of Science and Technology University (HSTU), Dinajpur-5200, Bangladesh','2012-03-02','First position from the undergrad batch','First position in overall results from the undergrad batch of 35 students. Among 8 semesters, consistently scores better to secure the position.');
INSERT INTO emran_honorsandawards VALUES(3,'Country Topper (Bangladesh)','South Asian University (SAU), New Dehli, India','South Asian University (SAU), New Dehli, India','2013-04-23','Post-graduation Entrance Exam','South Asian University (SAU) is a university established by the South Asian countries and students get admitted on a quota basis for each program. For the Master''s in Computer Science entrance exam from Bangladesh only the top 3 students were selected for the program. Scored top in that exam from Bangladesh.');
INSERT INTO emran_honorsandawards VALUES(4,'Best Employee Award','Advanced Apps Bangladesh (AAPBD) Ltd., Dhaka, Bangladesh','Advanced Apps Bangladesh (AAPBD) Ltd., Dhaka, Bangladesh','2014-07-15','Best employee of year 2014','Advanced Apps Bangladesh (AAPBD) Ltd. is a software development company in Dhaka, Bangladesh. For significant contribution to the company selected as the best employee in 2013-2024. During this time the responsibilities assigned were software application development, app testing, project management, client management and team management.');
INSERT INTO emran_honorsandawards VALUES(5,'BST Fellowship (BSTF)','BSTF Trust, Ministry of Science and Technology, Bangladesh','Deakin University, Melbourne, Australia','2020-02-21','Fully funded fellowship for higher education','Bangabandhu Science and Technology Fellowship (BSTF) is a prestigious fellowship under the BSTF Trust, Ministry of Science and Technology, Bangladesh. It is given to students who aim to pursue higher studies in Information Technology (IT) in top-ranking universities. It was received to pursue the Master''s program at Wageningen University of Research in 2019. Later, when selected for Deakin University and the fund was provided to study in Australia.');
INSERT INTO emran_honorsandawards VALUES(6,'Best Presentation Award','School of IT, Deakin University, Melbourne, Australia','Deakin University, Melbourne, Australia','2021-12-19','Annual School Conference','For the best presentation in the annual school conference organised by the School of IT, Deakin University in 2021. A 200 AUD prize money was given as the prize for winning this.');
INSERT INTO emran_honorsandawards VALUES(7,'DUPR Scholarship','Deakin University, Melbourne, Australia','Deakin University, Melbourne, Australia','2023-01-15','Joint Ph.D. Program & Funding (During study period at Deakin University) - DUPR','Deakin University Post-graduate Research Scholarship (DUPRS) was awarded for a joint Ph.D. program at Deakin University. The program was a cotutelle (joint) program with Coventry University, Coventry, UK. Tuition fees, Health insurance, and a stipend were part of this scholarship.');
INSERT INTO emran_honorsandawards VALUES(8,'Cotutelle Studentship','Coventry University, Coventry, UK','Coventry University, Coventry, UK','2023-01-15','Joint Ph.D. Program & Funding (During study period at Coventry University)','This part of the funding is for the joint Ph.D. program with Deakin University, Melbourne, Australia. Return airfare, Tuition fees, Health insurance, and stipend are covered in this studentship during the study period at Coventry University.');
INSERT INTO emran_honorsandawards VALUES(9,'AWS AI/ML Scholarship','Amazon Web Services (AWS)','AWS and Udacity','2020-04-23','AWS AI/ML Scholarships (Phase 1 and 2) for 2 Udacity nanodegrees worth more than 8,000 USD','AWS AI/ML Scholarships is a scholarship by AWS in collaboration with Udacity to help learn and apply artificial intelligence (AI) and machine learning (ML) in AWS technologies. I two phases (Phase 1 and 2) of this scholarship 2 Udacity nanodegrees worth more than 8,000 USD. A highly competitive test was used to select the top 2000 students for Phase 1 and the top 500 students for Phase 2 from Phase 1.');
CREATE TABLE IF NOT EXISTS "emran_languages" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "language_name" varchar(150) NOT NULL, "language_description" varchar(500) NOT NULL, "language_test_details" text NULL);
INSERT INTO emran_languages VALUES(1,'Bengali','Mother tongue','Excellent LRWS skills');
INSERT INTO emran_languages VALUES(2,'English','Medium of instruction, examination and communication at the universities where I studied and worked','IELTS (6.5) - LRWS (6.0,6.5,6.5,7.0) - 2019');
INSERT INTO emran_languages VALUES(3,'Spanish','Beginner level self learner at Duolingo',NULL);
CREATE TABLE IF NOT EXISTS "emran_memberships" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "membership_name" varchar(150) NOT NULL, "membership_type" varchar(150) NOT NULL, "membership_organisation" varchar(500) NOT NULL, "membership_institution" varchar(500) NOT NULL, "membership_address" varchar(500) NOT NULL, "membership_hasexpire" bool NOT NULL, "membership_start_date" date NOT NULL, "membership_end_date" date NULL);
INSERT INTO emran_memberships VALUES(1,'Advisor','Advisor','CSE Club','Hajee Mohammad Danesh Science and Technology University (HSTU)','HSTU, Dinajpur-5200, Bangladesh',0,'2014-09-01',NULL);
CREATE TABLE IF NOT EXISTS "emran_portfolios" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "portflio_platform_name" varchar(150) NOT NULL, "portflio_title" varchar(500) NOT NULL, "portflio_description" text NULL, "portflio_link" varchar(500) NOT NULL);
INSERT INTO emran_portfolios VALUES(1,'Github','DIHC_Downloader','A fully python based library to download the contents from a web directory including subdirectories and files.','https://github.com/WWM-EMRAN/DIHC_Downloader');
INSERT INTO emran_portfolios VALUES(2,'Github','DIHC_FeatureManager','A python and Matlab based library to do feature extraction and feature engineering related task for Machine Learning.','https://github.com/WWM-EMRAN/DIHC_FeatureManager');
INSERT INTO emran_portfolios VALUES(3,'Github','AWS_Udacity_AIML_Scholarship_Program','A python based Machine Learning and Deep Learning repository containing all the projects completed in AWS AI/ML Scholarship (Phase 1 and 2) programs. It contains total 6 projects from 2 Udacity nanodegree.','https://github.com/WWM-EMRAN/AWS_Udacity_AIML_Scholarship_Program');
CREATE TABLE IF NOT EXISTS "emran_projects" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_position" varchar(150) NOT NULL, "project_title" varchar(300) NOT NULL, "project_description" text NULL, "project_fund" varchar(300) NULL, "project_funding_organisation" varchar(500) NULL, "project_collaboration_organisation" varchar(500) NULL, "project_start_date" date NOT NULL, "project_end_date" date NULL, "project_image" varchar(500) NULL);
INSERT INTO emran_projects VALUES(1,'Project Research Associate','ANALYSIS AND DESIGN OF A NON-INVASIVE WAY OF MEASURING AND MONITORING BLOOD-SODIUM CONCENTRATION LEVEL USING NEAR-INFRARED SPECTROSCOPY.','Annually funded project by the university (HSTU) in 2018. It is related to designing a network security framework that is targeted for the maximum network security from DDoS attacks.','IRT Annual Research Fund','Institute of Research and Training (IRT), Hajee Mohammad Danesh Science and Technology University (HSTU), Dinajpur-5200, Bangladesh.',NULL,'2018-07-01','2019-06-30',NULL);
CREATE TABLE IF NOT EXISTS "emran_sessionsorevents" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "session_lead_name" varchar(150) NOT NULL, "session_lead_type" varchar(150) NOT NULL, "session_title" varchar(500) NOT NULL, "session_description" text NULL, "session_organisation" varchar(500) NOT NULL, "session_institution" varchar(500) NOT NULL, "session_address" varchar(500) NOT NULL, "session_start_date" date NOT NULL);
INSERT INTO emran_sessionsorevents VALUES(1,'Keynote Speaker','Keynote Speaker','A seminar on career development and future of Mobile Application Development in Bangladesh',NULL,'AFCSE','Hajee Mohammad Danesh Science and Technology University (HSTU)','HSTU, Dinajpur-5200, Bangladesh','2015-04-08');
CREATE TABLE IF NOT EXISTS "emran_skillsandtools" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "sat_title" varchar(300) NOT NULL, "sat_short_description" varchar(600) NOT NULL, "sat_description" text NULL, "sat_skill_level" integer NOT NULL);
INSERT INTO emran_skillsandtools VALUES(1,'Programming','Python, Java, Swift, Objective-C, C, C++, C#, SQL, PHP',replace(replace('Python: For research and development in Masters and PhD at Deakin and Coventry Uni. \r\nJava: For research and development of thesis work and mobile application in B.Sc. at HSTU. \r\nSwift, Objective-C: Industrial (development) level experience. \r\nC, C++, C#: Academic and professional (teaching) level experience. \r\nSQL: Academic and professional (teaching) level experience.\r\nPHP: Academic and personal (or in team) skill development level experience.','\r',char(13)),'\n',char(10)),100);
INSERT INTO emran_skillsandtools VALUES(2,'Datascience','Data Collection, Cleaning, Preprocessing, EDA, Analysis, Feature Engineering, Numpy, Pandas, Matplotlib',replace(replace('Data Cleaning: Missing data identification, Data cleaning, removal and imputation. \r\nEDA: Exploratory data analysis, univariate, bivariate and multivariate analysis and visualisation. \r\nData Preprocessing: Data type conversion, encoding, scaling, splitting. \r\nFeature Engineering: Feature removal, feature derivation. \r\nData Analytics: Statistical analysis, distribution analysis, statistical significance analysis, p-value, AUC, chi2, correlation analysis, mutual information (MI). \r\nNumpy: Data manipulation using 1D and 2D array, different array functions. \r\nPandas: Data manipulation using dataframe, different dataframe functions for data manipulation and visualisation (plotting). \r\nMatplotlib: Different types of plot and subplot drawing: scatter plot, line plot, histogram, bar plot, bix plot, violin plot, spider plot, area plot, group plots, etc.','\r',char(13)),'\n',char(10)),100);
INSERT INTO emran_skillsandtools VALUES(3,'Machine Learning','Concept and Application, Scikit-learn, Auto-ML',replace(replace('Concept and Application: ML fundamental, supervised, unsupervised, semi-supervised, reinforcement learning, ML algorithms, ensemble learning, data leakage, splitting, performance metrics, cross-validation, post-analysis, and pipelining. \r\nScikit-learn: ML concepts implementation. \r\nAuto-ML: PyCaret, Auto-sklearnm AutoGluon, lazypredict, TPOT. \r\nDarts: Time series data analysis.','\r',char(13)),'\n',char(10)),95);
INSERT INTO emran_skillsandtools VALUES(4,'Deep Learning','Concept and Application, Pytorch, Tensorflow, Keras',replace(replace('Concept and Application: NN structure and optimisation, ANN, CNN (1D and 2D), RNN, LSTM, transfer learning, transformers, VGG-XX, ResNet, AlexNet, and data generators. \r\nPytorch: Image classification. \r\nTensorflow and Keras: Image classification and time series analysis.','\r',char(13)),'\n',char(10)),85);
INSERT INTO emran_skillsandtools VALUES(5,'Health Informatics and Signal Processing','Disorder detection, Epilepsy, Sleep disorders, EEG',replace(replace('Disorder detection: Disorders related to epilepsy, sleep and ageing. \r\nEpilepsy: Epileptic seizure detection, seizure event detection, time series data analysis, EEG data analysis. \r\nSleep disorders: Bruxism, insomnia, breathing disorders, movement disorders, REM behavioural disorders, hypersomnia, nervous system failure disorders, etc. \r\nEEG signal: Time series data analysis, EEG data processing, data segmentation, feature extraction, EEG channel optimisation for specific applications.','\r',char(13)),'\n',char(10)),95);
INSERT INTO emran_skillsandtools VALUES(6,'Could Platforms','AWS, AWS Sagemaker, MS Azure, Azure ML Designer',replace(replace('AWS: EC2, S3, ETL, Scheduling, Sagemaker, AutoGluon. \r\nAWS Sagemaker: Sagemaker, Sagemaker Studio, Notebook, Lambda. \r\nMS Azure: Virtual Machine, Virtual Network. \r\nAzure ML Designer: Azure ML, Azure ML Designer.','\r',char(13)),'\n',char(10)),80);
INSERT INTO emran_skillsandtools VALUES(7,'Teaching and Training','Demonstration, Communication, Supervision',replace(replace('Demonstration: Demonstrate and illustrate concepts using intuitive examples. \r\nCommunication: Communicate information and knowledge, and get feedback for learning development. \r\nSupervision: Project and thesis supervision, and career consultation. \r\nEvaluation: Evaluate learning performances, give feedback, and suggest improvement plans.','\r',char(13)),'\n',char(10)),100);
INSERT INTO emran_skillsandtools VALUES(8,'Reporting and Presentation','LaTeX, MS Word, MS Excel, MS PowerPoint, Illustrator',replace(replace('LaTeX: LaTex report, LaTex beamer. \r\nMS Word: Document processing and reports. \r\nMS Excel: Data organisation and plotting. \r\nMS PowerPoint: Presentation and storytelling. \r\nIllustrator: Image editing.','\r',char(13)),'\n',char(10)),95);
INSERT INTO emran_skillsandtools VALUES(9,'Management and Leadership','Project Management, Team Lead, Client Management',replace(replace('Project Management: Software project management, task scheduling, reporting and feedback, milestone management. \r\nTeam Lead: Team management, task distribution, product testing and feedback management, task integration. \r\nClient Management: Requirement gathering, progress reporting and milestone delivery.','\r',char(13)),'\n',char(10)),90);
INSERT INTO emran_skillsandtools VALUES(10,'Soft Skills','Critical Thinking, Problem Solving, Communication, Collaboration',replace(replace('Critical Thinking: Problem analysis, critical thinking and analysis, questioning, interpreting, and evaluating a problem. \r\nProblem Solving: Problem identification, systematic solution planning, solution design, solution breakdown, section prioritisation, solution accumulation. \r\nCommunication: Presenting idea. \r\nCollaboration: Collaboration and team work.','\r',char(13)),'\n',char(10)),90);
CREATE TABLE IF NOT EXISTS "emran_volunteering" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "volunteering_name" varchar(150) NOT NULL, "volunteering_involvement" varchar(150) NOT NULL, "volunteering_cause" varchar(150) NOT NULL, "volunteering_organisation" varchar(500) NOT NULL, "volunteering_start_date" date NOT NULL, "volunteering_end_date" date NULL, "volunteering_detail" text NULL, "volunteering_link" varchar(150) NOT NULL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',1);
INSERT INTO sqlite_sequence VALUES('emran_languages',3);
INSERT INTO sqlite_sequence VALUES('emran_memberships',1);
INSERT INTO sqlite_sequence VALUES('emran_portfolios',3);
INSERT INTO sqlite_sequence VALUES('emran_sessionsorevents',1);
INSERT INTO sqlite_sequence VALUES('emran_projects',1);
INSERT INTO sqlite_sequence VALUES('emran_honorsandawards',9);
INSERT INTO sqlite_sequence VALUES('emran_skillsandtools',10);
INSERT INTO sqlite_sequence VALUES('emran_certificationscoursestrainings',11);
COMMIT;
