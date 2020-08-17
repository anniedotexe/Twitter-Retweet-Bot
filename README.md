# Twitter Like and Retweet Bot

[![Python 3.8](https://img.shields.io/badge/python-3.8-yellowgreen)](https://www.python.org/downloads/release/python-385/)
[![Tweepy Version 3.9.0](https://img.shields.io/badge/tweepy-v3.9.0-brightgreen)](http://docs.tweepy.org/en/latest/)

A Twitter bot written in Python using Tweepy and deployed on AWS EC2. It will like and/or retweet tweets that contain single or multiple keywords and hashtags. Default values of the project are used to run [@ac_celeste_bot](twitter.com/ac_celeste_bot).

<a href="https://www.buymeacoffee.com/awu2303" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" style="height: 45px !important;width: 200px !important;border-radius: 10px;" ></a>

## What You Need & Need To Know

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/) - a python package manager
- [Tweepy](http://docs.tweepy.org/en/latest/install.html) - an easy-to-use python library for accessing Twitter's API
- Make sure to follow [Twitter's Automation Rules](https://help.twitter.com/en/rules-and-policies/twitter-automation)
- [Amazon Web Services EC2](https://aws.amazon.com/ec2/) - a web service that provides secure, resizable compute capacity in the cloud
- [PuTTY](https://www.putty.org/) - an open-source terminal emulator, serial console and network file transfer application
- [WinSCP](https://winscp.net/eng/download.php) - a client that allows secure file transfers between the client's local computer and the remote server

### File Structure
```
Twitter-Retweet-Bot
 |-- config.py
 |-- credentials.py
 |-- requirements.txt
 |-- twitter-bot.py
```

### Instructions

1. Apply for [Twitter Developer Access](https://developer.twitter.com/en/apply-for-access) with the account you want the bot to be used for

2. Create a new [Twitter Application](https://developer.twitter.com/app/new) to generate your private keys, secrets, and tokens

![Keys and Secrets](resources-for-readme/keys-secrets.png)

- Make sure the app settings has *Read and Write* permissions

![App Permissions](resources-for-readme/app-permissions.png)

3. Create a file named `credentials.py` to hold the private information using the format below
    - See [File Structure](#file-structure) for where the file should be placed

```
TWITTER_API_KEY="xxxx"
TWITTER_API_KEY_SECRET="xxxx"
TWITTER_ACCESS_TOKEN="xxxx"
TWITTER_ACCESS_TOKEN_SECRET="xxxx"
```

4. Adjustments you can make in `config.py` to tweak the bot to your liking
    - `search_keywords` - Keyword(s) and/or hashtag(s) that you want to retweet
    - `delay` - Time to wait between processing requests in seconds
        - Please be aware of the [TwitterAPI rate limits](https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits)
    - `result_type` - Specify what type of search results you want to get
        - "recent", "popular", or "mixed"
    - `number_of_tweets` - Specify the number of tweets you want the bot to iterate through
    - `run_continuously` - Set True if you want the bot to run continuously
        - Also set True if you will be deploying the script
    - `retweet_tweets` and `like_tweets` - Adjust booleans for whether you want to only retweet, only like, or do both

5. Install Tweepy
`pip install tweepy` or `pip install -r requirements.txt`

6. Run the script. Enjoy your Twitter bot!
`python twitter-bot.py`


## Deployment

1. Launch an EC2 instance on AWS
    - See [Additional Information](#additional-information) for more details

![Launch Instance](https://lh3.googleusercontent.com/iOrAhLX9TyiTk4ZYq4SoE2EZ26g4B_VyZZ0_mtI1btpGayt6XzlfxmWdf4Oit28o38BQcHpPY0vgtUpJmBej6lo7Oyn2MFSIVOD-kZrRjtan4jVSP-NPVVPLuE0UQDMNIRkjer8a6bd7fHNbUPB642XXcDx3OdouOtqsAIt4h3SfGF8tC9gfsODJ7K7taiagLowRoP2Uc9TAEOfkVDQVzOrjBD4Q7U6895nMot-Ow5_nqWQuI1oFR6mchF05gOOCRgrygGWof98H5fYx27VqtsbnElU2mw7d7LdRjSXL9MR1mhqiOpwS3uhPRrav6fes120I2Hw1-0YMiCWOBPAJ2SnvGox7YDnPTB3kt6lpDT-31q__--27xZ-2Wb8u-wgKTp8jR0JbxOWDG5vbs_D8-waeVQwGXlyrBj1FFZu2l4REG7pTTyEtgGV8LQ8iVWPPHrmukNCwtgOFRElF873TZXEIA1xZey7j7HHPM5f951aVY2vuDgjRmmIjUAFwt7jC8qI2ZWtOXXZeNh8al3frKeqs2Z5kmqFKHjrJTnDDsjMeFOQUqz4b7-C2b4Zh-noLKOFAzKyRrQbYQct_xm8Oim03Fs39BT7ZyV6W8GVTJxJLyaHkCSkvYXHE49GWds1zUOCM9pX0HTW7xjIcRzJpRbNhrfFitvPsWtUqR_h3xtYMmiJk8siu-afNug1aMDI=w1920-h937-no?authuser=1)

2. Load the key-pair file (.pem) into PuTTYgen (which was downloaded when you installed puTTY) and save the private key as a private key file (.ppk) 

![Generate PPK](https://lh3.googleusercontent.com/-zXTZ34PRNLoICgXoReP7rBSuS67nC_8qVEZ7NC7EOhK1gH12JunjA4azOXyckSMV3HgrZq5M_AD62PnzTAmVBs4LgF0zG1jRYJyfZNZW0gg-rkS5ADO5xfbjHHDZZKRHSy3SIT0X8RHa-GOsOpEacymCDDUTB8yAqjI9f-ydldwVgaY66A1U2XSN65LF_jn7jmQtIKdxiuxlA2cPYQpk_Tk-o6tmgj8VGxvtqh41gQNApdH_Jl5saeStOvsaKGqRiQqHZ4fpECg_YnfNSo2qiLaSGYEcDOubdkDtXyNWf0BAadCwy-YVXi0Dob0lDXVVoZfwqumVfT9QS9O1sgQ2gQKdqByN7tLGFTwxbAf6R-B6-kxbrW_BBQCRJ9iUwOQE6J3qQzLuP0ClmlJO6WUSm8r-bqhAl-aS3twkCilgxxbpFXjFmXnQX98CxmG27ADUdxQ-Dt6aCWIEhaJXIYckH2Rgl9mb4xcPyix7xqNW2lupeSC4_sgyGcLsXh0Mj5vP6iuuERymWplvEaIW12fv3vlyIV2uOm8s-Y4BA17nTfKc8QMJoaTXgWm09AqgimcOCM5qOkedVeHSGDhr28Cvsfr_r1_0FIBmbooI6qxqXPrXNw3mBhOIiZxM99ek39rqgwJc-oMw2TFahoGKzp-rNYzV_2SvOPqYyxmOSXjx8-2SRBWJfeSMJDgHrVlMA=w1350-h773-no?authuser=1)

3. Connect to your instance on WinSCP
    - The host name is ubuntu@[public DNS here]
    - Click Advanced, go to Authentication under SSH, and load the previously generated private key file (.ppk)
    - Login to the session

![Connect Instance to WinSCP](https://lh3.googleusercontent.com/beZRWgRMEv1cpw2hRg3D-HfMNpdedyC50OIPXrbEMTsr6lRMwHODHZZUeYZNmocupzqM30l68AxF7yIrrmMpdckfcirYxx_EM9Lu2dOXIN-yjzwD0rOqsn6vqJcGen0b1_73oBAVjGNpLLamH8e9EgRDB0bMcyzEroK4cCPZrCk_rfwRjgNnnAEdHf-oWtftgIo8K3CXhlywxnzngISOYxfMAQGxnsHZqlfbEN4yhIv_p47Z0_qUqUyaajuhZn1m8feEV_IZsLesRwXiAebsZTJUx6NzatLHG6Vgk7EHj5Gfmp8dxcr4wSZsnL_QeAuIuk1R3mTW9cvZx4SfL4xdx2_2DhAzEwM-FrmzmhpYWRXtAwX6Zb4XmLeKuG3ZR7Of6JWnY9z4i--pXJA4Rl_V7NtNMw1MDydleIezH2F2bauwC8lNnWktzlHEkIEonwNyw9JOoi7d0b9p46NdYV-v8AfliVJ0u8_6d-Vchwn3U3SItaWJwZ1VmgnJk_wFhXrvw0-dEEzveyyfERgirbBsDWd8LIJGWqDc4gk63jYzLGMbpPgJx_vw2Evknn2g6Ag_p5hS93hoS6djOjpP9DgUiCUFiBSCa-l6zmFWX-I_A5rsH3knzA01PpgYYXTFabTFlLNRa6ytDEipbXrte65TZkTEBZbLDsBJTUKcCri5EVXQ1mO6EZIJb1S5cIevUg=w1920-h937-no?authuser=1)

4. Use WinSCP to transfer the project's .py files to the server

![Transfer Files](https://lh3.googleusercontent.com/jUVmIcCe-fo7bLk3MPcs6h_7ff4O9Oi1PHcqxxiP5QbhyliphoDvjzHSf0K_KgygfqGyS3RFm8aRUlef2VQBdMClXbiz4cpoVWdmI3jEsaI0GQfzOQdoofBt08m6-iS6HiwLpgLvWtCSh1vV48cGkDNYwqHj9iqDia-tVKYUbkLYsDuMhoYfkDXmfU--IBtmCQRF3yHCfwbvfIgpzpfN1rkbkCs9RqX1tEQSO5ndUIfgOeDEPmPYdkjNTl9G8JMtNFpDw7O9UdV5ceOzjV0bOfE9GBdLgIgZHFB_J_cDdlYYvCUeLPz0n7G6Gh1MktM-qB2lJDYTv3cj404vS2UmB18nqHayOLwRT5lFL5TLlxHo29WfQ5mGoV89NRcxqcnjUEjL6egsak8Ky7hKSpGlbT579TWmClm9mQ9dtqjVY4VX_K1Wqlaypg6a3CY_lu3GoTMccspT0kmvZZa_uvoG5rWJP_sM1XSyocCVn8mh0pCB8aKyuhiUeazkTa5rqV0FKK5BKj30z8umDg0VHfJTN4AtvzggYTL8u9NIm8nWFfxjtyqhBv9JPKMS8WlS6sEQ-1RoAK_EEGeefYmn4KG2KCps2wSlapbxTo9DE6nXQ677gUwP7XNK3r8SD1G_rApAdo4SIlK_0zsrjK1eWPXk7px0a7ctJ8Ucyf4an-UD1go1ziNn5XKhK9k1swQTeg=w1076-h693-no?authuser=1)

5. Connect to your instance on a bash command line using one of the following ways
    - Use a bash shell with the example ssh command (I use [Git Bash](https://gitforwindows.org/))
        - Make sure you are in the directory with the key-pair file (.pem)
    - Use [PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html?icmpid=docs_ec2_console) with the public DNS and private key file (.ppk)
    
![Connect Instance to Bash](https://lh3.googleusercontent.com/q7D5VRizYlJwXKpachujseTDZb5ybWsCfE1UP-Tl7-0DCMTE7QBVb3R7cKzJIrWf5GeXuMT_cRNIthuFTXEYsF0P4hnDB2hm7BNuyDiw2AdCbV_NrQ2jUP-ZZbNBhXd-xUa6vy-2gL0NseLXX3X1_xO4ZQS8Ge34Wy7IxUEU-4Fc6xdJQ2svod9ksHBJMbB83gYRZkHPTOaVOnqQWlmvkrnUkmXbc6dPCQsG-bpaY6bm-CTJ6CxcO3uzBZI5I3ChY9cXmFBgANEMoJg8fU7dWn7sYui6Ft6ypWmdesJ7H6zcZ1iO3eE2DHD52Szmuw6CB4JcL1XwbAkl44S_HAC051QBumz_xVFv3_zkf_7WELvXM1fojNyRnCCqqxhYZxklxj35_x94Pg2_AobS-I7yt8NOOBlrWvqiFp9rtcxinId8lsBiQ7y3jC6zoJQdNK8fQGDNueYoz_MQLl3NdAmyhRGVH4WQxD9uiQ_myT2EO3inwxJVvyym61SgW2KAhbo73AmiGJZHkkmDrspephce1-uDl1CFeIuvesl6BUAgDgd5c2UnjzoqnNQjM-Ss32vxmUgmuEQEpdEd9jt6yQW_M1rxG-9uOJXMreCNGDKG0sqJ6muB6yHmIGrFJq3luDUu1RM7mxUfaeq4QHaEx-tPxI4kFYORMIQbxQDo-xUm1KxjwvbEju8rrnVP6-6tPQ=w1920-h937-no?authuser=1)

6. Install python and pip to the server on the bash command line
```
sudo apt update 
sudo apt install python3
sudo apt install python3-pip
```

7. Check if python and pip have been installed correctly
```
python3 --version
pip3 --version
```

8. Install tweepy to the server
`pip3 install tweepy`

9. Run the script. Enjoy!
`python3 twitter-bot.py`

10. See [Additional Information](#additional-information) for details on running the script continuously on EC2 server
    - I use the `screen` option

## Test Running the Script

Test `config.py` values:
```
search_keywords = "%23overwatch OR %23mamamoo"
delay = 5
result_type = "popular"
number_of_tweets = 5
run_continuously = False
retweet_tweets = False
like_tweets = True
```

![Test Run](https://lh3.googleusercontent.com/foOESASjEFCvBRmRVpAOL9xbPQ4BVmtmkrhnaUySAxMDksZyee9uVlK74_bllYI-nF71_wH4QRJUl6SgPp02l_5odOBjTqQy1w1wMN8n7FlwX7LBs33ajF1r5yLCAFQSA5wjioPTtpcQWGTGPplUmnJfZH0WvwF-OkEbv5HHllUH9IaiFm25NXh3C3caP6QXdmkDZcMVu4pCKPw6944OSYOvjKcGnYkKe72chSwaNVbtm2WJZgxqbRIFHyyTRCHRO0WvmgmMALCklMC1hFqunqhDRY4M3lT79eHpEOYrQupmCngGD9M6yv7xoFTyDTVAWWO0h3TDqadBvonny2xR9QaEGKBVIEYXydRk5QDctjaNzhyRw51w9pMadB1hPd8cUkoAU_18rpNK8EZf7b0_y3CsdgJv1i7OIPBtWq4p-NlGmP1juoukGXn-_keQtQXnR1VCj8WRrlnbwQx5_XVJIPUwb1rktIKtcmtOvaHl2Xku7Xvtsm3YeT4jchqsSZLweTuKjLSppbUNFMJKuGMLvM3kNqFxX5HQcMdX0jGM-q0JbAaWNaYz2273c0jyyavWSDaQziy6cEGw6MQLsMWfjI_Vr-iNUXnF-iTjzEvN9J3mKbSLDWMxpCMPXWNjUITxChvT2kYKCLy675xQEHCH2VMDztzJvq0Ig-M3pgWTKklBtvATI-wddlmpq8ZLeA=w979-h452-no?authuser=1)


## Additional Information

- [Getting Started with Amazon EC2](https://aws.amazon.com/ec2/getting-started/)
- [How to Continuously Run a Python Script on an EC2 Server](https://intellipaat.com/community/9361/how-to-continuously-run-a-python-script-on-an-ec2-server)

