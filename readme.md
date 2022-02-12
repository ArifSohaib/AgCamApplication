How to install: <bn>

Type the following in your Raspberry Pi Termainal


clone the repo
```
git clone https://github.com/ArifSohaib/AgCamApplication.git
```

navigate to the correct folder
```
cd AgCamApplication
```

Install the required libraries
```  
python3 -m pipenv install 
```

<em>There is currently a bug where one of the libraries isn't installed properly fix it as follows

activate the python environment you installed
```
python3 -m pipenv shell
```
within the environment, install imageio-ffmpeg
```
pip install imageio-ffmpeg
```
exit the environment
```
exit
```
</em>

allow it to run as an executable
```
chmod +x main.py
```

Start the app
```
.\main.py
```
Or click the main.py file