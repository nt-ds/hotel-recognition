# Hotels Against Trafficking



## The Very First Step to Battling Sex Trafficking



### Motivation
<img src="readme_images/motivation.jpg" alt="motivation" width="200"/>
In the United States alone:
- Approximately 75-80% of human trafficking and slavery is for sex
- 30,000 people die each year while being trafficked for sex from neglect, abuse, disease, or torture
- Nearly 20,000 victims are sold and trafficked each year. This number includes the victims who are as young as 5 and 6 years of age
- There have been approximately 100,000 to 150,000 sex slaves since 2001

Source: [The Disturbing Reality of Human Trafficking and Children](https://www.huffpost.com/entry/disturbing-reality-human-trafficking_b_8831834) (Dec 18, 2016)

--------------------------------------------------

### Objectives
**Problem**<br>
<img src="readme_images/problem.jpg" alt="problem" width="200"/><br>
Commercial sex within hotels and motels are most frequently advertised through online platforms (Backpage.com, Eros.com, etc.)<br>
Source: [The National Human Trafficking Hotline](https://humantraffickinghotline.org/sex-trafficking-venuesindustries/hotelmotel-based)<br>

**Goal**<br>
Automatically classifying different hotel chains using Deep Learning

--------------------------------------------------

### Images
Images are obtained following instructions from [Hotels-50K: A Global Hotel Recognition Dataset](https://github.com/GWUvision/Hotels-50K). However, for this project, we only focus on 3 hotel chains:
- Two-star hotel chain, Comfort Inn
- Three-star hotel chain, Best Western
- Four-star hotel chain, Hilton

We also only use a small subset of these hotel chains' images. The training set contains 12,000 (128,128,3) images. The validation set contains 3,000 (128,128,3) images. These two sets are obtained using [sklearn's train\_test\_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html). The "original training set" contains 5,000 (128,128,3) images of each hotel chain, totaling 15,000 (128,128,3) images.
