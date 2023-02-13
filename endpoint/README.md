# Endpoint-Checker
## What is this ?

Endpoint checker is code made in python,wich allows you to test your **own endpoints**, on a **specific URL** to see if they are valid.
This code is **open source**, feel free to use it but give me credits ;)

## How it works ?

### Get the code

You copy the git repository by doing: 
```
git clone https://github.com/ArtyETH06/Endpoint-Checker
```

Then,go in your repository:
```
cd Endpoint-Checker
```
### Download the depedencies

To download all the depedencies necessary to the project,you just need to do:
```
pip install -r requirements.txt
```

It will download everything you need ;)


### Setup your lists

You can change the 2 lists: list1.txt/list2.txt

-For the `list1.txt`,you can put the **endpoints** that you want to test.

-For the `list2txt`,you can put the **websites** that you want to tests (for a specific endpoint).


### Start the tool

You can run the python file by doing:
```
python endpoint.py
```

Now you have the choice between 2 modes:

![Capture d’écran (701)](https://user-images.githubusercontent.com/107058122/213551832-8936658c-2fe2-4497-b383-22b3d7888ec8.png)


#### Many endpoints for 1 website

This mode will take all the endpoint of the `list1.txt` and try them on the URL that you will have to choose:
![Capture d’écran (702)](https://user-images.githubusercontent.com/107058122/213552058-854a437e-02e2-44d1-87d7-72d6a82ad14d.png)

#### 1 endpoint for many website
This mode will take all the website of the `list2.txt`and try the endpoint that you will have to choose:
![Capture d’écran (703)](https://user-images.githubusercontent.com/107058122/213552611-da2b8905-2cfa-4bb3-8493-71a5cb377c68.png)

### Save the results

Once the scan ios completed,you will have a list with all the valids endpoints,you can save them in the files `endpoints_mode1.txt` or `endpoint_mode2.txt`
For that you juste have to enter `y` (who stands for yes):

![Capture d’écran (704)](https://user-images.githubusercontent.com/107058122/213553081-79e49aa2-3046-49ba-9890-84daece8fa4e.png)


That's it ! You can now use the tool as you want !

Arty06
