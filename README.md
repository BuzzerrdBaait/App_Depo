<h1>App Depo</h1>

<h3>Task and Purpose:</h3><p1>To deploy and continue building reusable Django apps. To share Django knowledge for the love of programming!</p1>

<h3>Welcome</h3><p1>I have been buildling in Django for a little over a year now. I host two web apps currently. www.ilovecookbooks.org and www.flashcardzz.com. So my short term goal is to house both of these under one roof "App Depo".</p1>

<h3>Goals</h3>
<li>Find people who want to develop or learn how to wire in urls,create models,views,forms,ect.</li>
<li>Create helpful documentation</li>
<li>Create apps together so I can learn how to work as a team player</li>
<li>Add ilovecookbooks</li>
<li>Add flashcardzz app from flashcardzz.com</li>
<li>Continue building features onto ilovecookbooks and flashcardzz</li>

<h3>Screenshots of flashcardzz.com</h3>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/2b385c91-a100-49a5-8f79-7018eda095c9" alt="Not Found" width=90%>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/217f6619-64fc-414c-ae9a-bc7cb085f697" alt="Not Found" width=90%>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/d0d1ecf0-e3ee-4815-9e11-1f0773d3482b" alt="Not Found" width=90%>
<h3>Screenshots of ilovecookbooks</h3>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/18b3a022-6c34-456f-8943-e8c13e66ca55" alt="Not Found" width=90%>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/c6473dcc-4f8a-46c7-bc79-35d7c5bda271" alt="Not Found" width=90%>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/4d807850-1383-40a7-b11b-9de3e75932bc" alt="Not Found" width=90%>

<h1>Getting started</h1>

<h3>What you will need</h3>
  <li>pip installed. Newer versions of python come with it. </li>
  <li>git hub CLI installed: <a href="https://www.codecademy.com/article/the-github-cli-command-line-interface">Geeks for Geeks</a></li>
  <li>python</li>
  <li>mysql workbench or choose your own database</li>
<br></br>
<h3>Installation can be summed up like this</h3>
<p1>1. First thing, create your virtual environment</p1>
<p1>2. cd into your virtual environment's scripts folder and activate 'activate.bat.</p1>
<p1>3. Clone the repository</p1>
<p1>4. cd into the new app and install requirements.txt<p1>
<p1>5. Create your secret key. Store it in the system environment variables</p1>
<p1>6. Open 'cmd' line and migrate</p1>
<p1>7. Run py manage.py runserver</p1>


<h1>By the steps..:</h1>

<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>

<p1> 1. First thing, create your virtual environment</p1>
<br></br>
<p2>Open cmd line and cd into the directory you would like to store your virtual environment</p2>

```sh
cd desktop
```
<p2>Create your virtual environment, this takes a few seconds.</p2>

```sh
python -m venv App_Depo
```

<p2>this creates your folder that looks like this</p2>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/4e1a70bd-4dd0-499e-9a18-2c62c8e9021b" alt="not found" width=65%>



<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>

<p1> 2. cd into your virtual environment's scripts folder and activate 'activate.bat.</p1>


```sh
cd App_Depo
```

```sh
cd scripts
```
<p2> Then activate your virtual environment</p2>

| cmd line  |powershell.ps1| 
|-----------|--------------|
| activate.bat|./activate.bat|

```sh
activate.bat
```



<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>

<p1>3. Clone the repository</p1>


```sh
git clone https://github.com/BuzzerrdBaait/App_Depo/
```


<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>

<p1>4. cd into the new app and install requirements.txt<p1>



<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>



```sh
cd App_Depo
```


```sh
pip install -r requirements.txt
```

<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>

<p1>5. Create your secret key. Store it in the system environment variables</p1>

<p2>Open the system search and type "Edit system environment variables"</p2>

<br></br>
<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/fe64c3cc-4dd6-444b-b5fb-02712bdfb2d3)" alt="Not found"> 

<p2>Click 'Environment Variables'</p2>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/cba593bd-7bf3-40ea-9c0a-06535e1cc33a" alt="Not found">

<p2>click 'New'</p2>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/e09d55fe-315a-43e9-b42b-f8a5a4087677" alt="Not found">

<p2>Create your new variable like this.</p2>

<p3> DJANGO_SECRET can be any random string, just make sure it is like 20 characters long for good practices. <p3>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/c4636ed2-276e-4de3-8c23-e8cb97578373" alt="not found">

<p2>Press 'Ok' to save the new variable</p2>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/3bc96557-a53b-42ef-971f-cd1d87cfc3c5" alt="not found">

<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>


<p1>6. Open 'cmd' line and migrate</p1>

<p2>if you are not in the directory containing manage.py, cd into your project's root directory</p2>


```sh
py manage.py migrate
```


<br></br>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<p1>_.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-._.-.</p1>
<br></br>



<p1>7. You should be ready to runserver now</p1>

```sh
py manage.py runserver
```

<p2> hold ctrl + left click the ip adress here </p2>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/3ffa5b38-c73b-4980-ad3b-e4e62b08f743" alt="not found" alt="not found">


<p2>This should open up a rather bare home page</p2>

<img src="https://github.com/BuzzerrdBaait/App_Depo/assets/108156235/b5b70220-e499-4741-ae29-e72da65fc4e2" alt="Not found">


<h1>Wooooohoooooo!</h1>
<p1>You are now running the app with an SQLite Database.</p1>
<p2>It is important to set up you database to maintain persistance amongst multiple sessions</p2>

<p1>I will be adding more documentation to help users get comfortable with the layout</p1>
<h1>Thanks for reading!!!</h1>


























