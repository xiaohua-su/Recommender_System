# Recomender System

![img](./images/Hulu_Banner.jpeg) 
### Authors

- Jawwad Siddiqui:
[LinkedIn](https://www.linkedin.com/in/jsiddiqui85/) |
[GitHub](https://github.com/jsiddiqui85) |
[Email](jsiddiqui85@gmail.com)
- Kyle Weesner:
[LinkedIn](https://www.linkedin.com/in/kyleweesner/) |
[GitHub](https://github.com/KyleWeesner) |
[Email](weesnerkew@yahoo.com)
- Nimeshi Fernando: 
[LinkedIn](https://www.linkedin.com/in/nimeshi-fernando2019/) |
[GitHub](https://github.com/nishlikefish) |
[Email](nimeshilfernando@gmail.com)
- Xiaohua Su: 
[LinkedIn](https://www.linkedin.com/in/xiaohua-su/) |
[GitHub](https://github.com/xiaohua-su) |
[Email](xiaohuasu99@gmail.com)
- Zachary Rauch: 
[LinkedIn](https://www.linkedin.com/in/zach-rauch/) |
[GitHub](https://github.com/ZachRauch)|
[Email](zach.rauch0@gmail.com)

## Overview
<br />
The aim of this project is to build a model that provides `top 5 movie recommendations` to a user, based on their `ratings of other movies` from Hulu. Our audience in this case is the **Hulu Technology Team** headed by the *CTO* of Hulu. They are holding a competition to upgrade their current machine learning algorithm that oversees the movie recommendations given to a Hulu subscriber. 
<br />
# Business Understanding and Stakeholder
<br />
Todays streaming landscape is vast and diverse, with over *1 billion users worldwide* and generating over *500 billion dollars* in revenue.  Hulu currently holds *14% of the market share* within the streaming industry, trailing behind **Netflix** with *25% of the market*, **Amazon Prime Video** with *18%*, **HBO Max** with *17%* and **Disney Plus** *with 14%*.  It's also important to note that *85%* of **Hulu users** are also subscribed to **Netflix**.  Currently, Hulu uses a *item-based collaborative filtering algorithm*, this is a successful approach commonly used by many recommender systems. This type of recommender system takes into consideration the ratings given to movies and shows by users as the sole source of information for learning to make recommendations. 
<br />
Currently, Hulu is *losing their customer base* to their competitors **HBO Max**, **Prime Video**, and **Netflix** to name a few.  Although, Hulu *currently holds 14%* of the streaming market share - we want to ensure Hulu is able to maintain their subscriber-base by *increasing their user engagement* with their platform through *the implementation* of our improved recommendation system.
<br />
## Data and Methodology
<br />
The data was gathered from **GroupLens.org** where the information within this dataset is from **IMDB** and **TMDB**.  The rating and movie information was captured between the years between 1996 and 2018.  
<br />
The dataset has over **100,000 movie ratings** given by **610 different users** for about **9700 movies**. Each user had reviewed *aleast* **20 different movies**.  However, due to time constraints, our model was built off of **100,000 movie ratings** versus the **1.9 million** ratings that were available in the original dataset.
<br />
## Results


## Next Steps


## Conclusion


## Repository Structure

```
├── Workspace  
│     ├── Jawwad
│     ├── Kyle
│     ├── Nish
│     ├── Xiaohua
│     └── Zach
├── data
├── images
├── .gitignore
├── LICENSE
├── README.md
├── Recommendation_System.ipynb
├── app.py
├── mac_streamlit.yml.yml
└── windows_streamlit.yml
```

## Citations:

Images:
- https://streamingwars.com/whats-leaving-hulu-this-week-from-50-first-dates-to-rambo/
- https://towardsdatascience.com/recommendation-system-series-part-1-an-executive-guide-to-building-recommendation-system-608f83e2630a

Code References:
- https://github.com/danielburdeno/Kindle-eBook-Recommendations
