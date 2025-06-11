# Features Explanation :

1. "content" : This contains the tweet text. 
2. "has_media" : Tells whether the tweet has media or not
3. "hour" : Time at which tweet was posted.
4. "word_count" : Number of words in tweet.
5. "char_count" : Number of characters in tweet.
6. "sentiment" : Tells the emotion of tweet if "0<" then tweet is positive and negative in case of ">0".
7. "company_encoded" : Encoded names of company in numerical form for training model
8. "day_of_week_encoded" : Encoded names of days of week for training.

# Model Improvement :

## **Modification - 1** :

At first I was using raw likes and above features giving RMSE ~ 3000. But then I used sentence embeddings from sentence transformers which reduced it to ~ 2400.



# **NOTE** : Below modifications were performed mistakenly on a lower datasets that's why rmse got lowered but i tried these also.

## **Modification - 2** :

To further improve RMSE, I used log of likes (as likes are inconsistent) in training my model.This improved my RMSE to ~ 1800.

## **Modification - 3** :

Now I was trying different text extraction methods in which using TF_IDF showed good value of RMSE (~1500). So then i used it instead of sentence transformers.

## **Modification - 4**

I checked values of RMSE at different values of max_features in TF_IDF. In which i got RMSE is minimum(~1200) when max_features in TF_IDF is 40.
At first max_features was 1000 so i reduced it 40.
This also improved my R<sup>2</sup> from -0.96 to 0.12.

## **Modification - 5**

Used LightBGM instead of randomforest with one more feature of average company likes. Final RMSE : 1020 , R<sup>2</sup> : 0.29
