#Important!The Google Cloud Speech Credentials are valid only 4 hours
#After being created by ACloudGuru Google Cloud Sandbox
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# recognize speech using Google Cloud Speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
  "type": "service_account",
  "project_id": "playground-s-11-0f03bd7b",
  "private_key_id": "5b19befe67f1806580475c2677d238eedd876278",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCp1cMPtRWsZNBK\nTBW0pyYL+bQEjg0u/B3ekDcuSF7oNsk0nxlckWKeKrMbS6RlENti6O3pov9ZvpRn\nFBWQSvsii/c+w6eC1AYo1SENAoPGrUa2dsjkclKX5lxWYQky/6FCKUrkMgDjGAU6\n4PdE6AEcObHS5C1xWsCw/Za27mdc9znl54/BcMz+pZtvSeR2IOqOIY8Q49W60qJv\nSOlHz1NaII0irRgunW8Q1ueDqwNP4FwqHvHDiuhRh4lK2wgjr3YIoOlUGUTeyc8y\noUHy508zfK4xegPk967/3kdV+9SaBd/e3gDVTj8vKP/s1XkZdHLbe0nEPLI8hl+S\n4lSmNiltAgMBAAECggEAKB43oqk7AmsaDMLmSbNGOIP2szC/Cn9BqwZUEpnD2YS/\niK+gdQ5exk/92Q/IOJt/x2CQeqUnPpLXSXYkFd6wbhuz/t6G3k+pWNHnqcQTTsY1\nsvpiQByFSB6BZ2IqoyJhfFh2uWrabMqKybrEjkFjqcAzMkb2ORWf+O8eP/4W6o2V\nWlQAnEqLW2mqlvzXoGJctxR6FTNeOW84VKHtzH1Xj43IaKncYjsBCwdRKFv7ULGB\n/sYj82CETcNdGYXOjCRU3j6eEviMDxz9eJI2yuDIbx8U8BUaieolwBYwy9f+WpEz\nRlJexBpg64nRKGNRlevyAuV3omgMxds+sDnR2xtBIQKBgQDS5/4z34adVGAHBwX6\nMFZ//0eN1ReZlBt4fpT5NDWXwBc/gKoVP/C1jvMpvx+KQMP9vjcM+tzHgUbiR0kp\nBnBsktjnARBlzC7UcFWYUk2oGJ5iqQdbF/8v1XGVyuGEbYj3Bkya1u7JD9H4U8kN\nDuGUHVpYQeArYDl4vhoehEW+CQKBgQDOJbmvfFRBqE23MGXv13XDx/cSt8e/H26f\nXh60yWIBGx0hihh90BNxuOqzNNMdK+/KtrbZ7W7QygpVJORnTxKJjtvlqDQQX5Ci\ndju7ZwcJLxV1ocftZLKFLlx5J1eYA+HEhf2120v7LPhlmphWQkar5VhZHKJ9RV9U\nrLj2qsapRQKBgQCLWenmEFz7exJv0j4qzuF4dQ2sMw4C1Y9JECoSdmKqv6sctECt\nBbBf5fHYtYV7bcuRzqrFEsPptgtF22AFkVGbC3PxPgy9limjCA4mNMtGs+2Ctrg7\ngiGEU31XQdO8EjubLDhVXoorox5S+9ktnZWCrdpR0kTxpASVONY9L5x9MQKBgHH3\nCzOH0XDG4cf/eqtgext0RhRUA5qWfuqd9u3NU1/3JGCxXp7XVJiPOTk/X+MFsjho\nUKgkChplR9cQYTD31vCzSMArADV5D5WxNY6CA7LBE+UHPmbwP30/RyI3bMZ+hubF\niKBsDxJaJyzMjaFKXJWVYgVJvk7w9iXyowLDILbdAoGBAMEPz92Dfh0c+rRYKX+Y\n3VX0P+w8m+ivodWVhymp3Sa9EJ+Dafxeh32JMW+G3VXkmWJu2MFSNDDxxs/snUtA\n3fTRKIH7DFY3ZQNSms6kIt+VLb3vrBYMW38u6d4XJ3ZM73peVyyhS2q/z89pSagW\nZphNgmlJi3CvaHNY5lt+vUJf\n-----END PRIVATE KEY-----\n",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/playground%40playground-s-11-0f03bd7b.iam.gserviceaccount.com"
}"""
try:
    print(r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
except sr.UnknownValueError:
    print("Google Cloud Speech could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Cloud Speech service; {0}".format(e))
print(r.recognize_google(audio))
