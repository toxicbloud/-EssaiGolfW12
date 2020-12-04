from datetime import datetime
import tweepy
import time

APP_KEY = 'ahbahouicajedonnepas
APP_SECRET = 'canonplus'
OAUTH_TOKEN='celuinon'
OAUTH_TOKEN_SECRET='etEncoreMoinsCeluiCiLemieuxcestdemettretesclefsdAPIdansDesVariablesdEnvironnement'

auth=tweepy.OAuthHandler(APP_KEY,APP_SECRET)
auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
api= tweepy.API(auth)
while True:
    message='Dites voir @VWGroup @vwgroup_fr @vw_france vous voudriez pas prêter votre Golf GTI W12 à @VilebrequinAuto pour un #ThePetitTour ? Ce serait sympa de les rég$    api.update_status(message)
    time.sleep(1000)