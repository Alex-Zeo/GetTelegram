import pandas as pd
import time
from datetime import datetime
from pytz import utc
from tqdm import tqdm
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import FloodWaitError

#config
api_id = 'boigetyourapikey'
api_hash = 'geryourownhaskhey'
phone_number = 'sillygoosewhatsyourphone'
start_date = datetime(2024, 4, 1, tzinfo=utc)
end_date = datetime(2024, 4, 30, tzinfo=utc)

# List of channels to mine
channels = ['@+8Rah-lb7Q6Y2MjQy',
            '@+dUuGAwrf1ckxNWI8',
            '@ab3army',
            '@AFUStratCom',
            '@agurulev',
            '@akashevarova',
            '@aleksandr_skif',
            '@andriyshTime',
            '@annamaliar',
            '@astrapress',
            '@ASupersharij',
            '@babchenko77',
            '@BattleSailor13',
            '@Bayraktar_News_UA',
            '@bmrada',
            '@boris_rozhin',
            '@boryslavrada',
            '@brussinf',
            '@brygada47',
            '@ButusovPlus',
            '@CinCAFU',
            '@concordgroup_official',
            '@Damhistory',
            '@DCSpeaker',
            '@DIUkraine',
            '@DmitriySteshin',
            '@dnepr_operativ',
            '@dnipropetrovskaODA',
            '@dnronline',
            '@dshrg2',
            '@dva_majors',
            '@epoddubny',
            '@EurointegrationComUA',
            '@geromanat',
            '@GrafinyaNegoduet',
            '@grey_zone',
            '@gruz_200_rus',
            '@guildhall',
            '@i20028843',
            '@igor_korotchenko',
            '@infofakt_ua',
            '@insiderUKR',
            '@intelslava',
            '@ioannZH',
            '@itarmyofukraine2022',
            '@ivankivINFO',
            '@kaagranovich',
            '@kharkivoda',
            '@khersonskaODA',
            '@kievoperativ',
            '@KIMMARINA',
            '@kolomyiagov',
            '@kurtievofficial',
            '@KyivCityOfficial',
            '@kyivindependent',
            '@kyivoda',
            '@Kyivpost_official',
            '@landforcesofukraine',
            '@LastBP',
            '@legitimniy',
            '@liganet',
            '@liveukraine_media',
            '@logikamarkova',
            '@lutskradanews',
            '@lvivmediacenter',
            '@Mestb_Dobroj_Voli',
            '@milinfolive',
            '@mod_russia',
            '@montyan2',
            '@mykolaivskaODA',
            '@news_kremlin_eng',
            '@niklive',
            '@noel_reports',
            '@Novoeizdanie',
            '@novynylive',
            '@O_Arestovich_official',
            '@odeskaODA',
            '@ok_spn',
            '@oleksandrmamay',
            '@oleksiihoncharenko',
            '@operativnoZSU',
            '@our_odessa',
            '@pavlokyrylenko_donoda',
            '@pilotblog',
            '@polkazov',
            '@povitryanatrivogaaa',
            '@PpoUARadar',
            '@ramzayiegokomanda',
            '@readovkanews',
            '@rezident_ua',
            '@rlz_the_kraken',
            '@RSaponkov',
            '@rsotmdivision',
            '@RtrDonetsk',
            '@rusich_army',
            '@RVvoenkor',
            '@rybar',
            '@SBUkr',
            '@SergeyKolyasnikov',
            '@serhii_flash',
            '@sheyhtamir1974',
            '@shot_shot',
            '@shurygin_vladislav',
            '@sirena_dp',
            '@Sladkov_plus',
            '@smotri_z',
            '@SolovievLive',
            '@southfronteng',
            '@spletnicca',
            '@SrbijaRusija',
            '@starukhofficial',
            '@stranaua',
            '@strelkovii',
            '@suspilne_vinnytsia',
            '@suspilnelviv',
            '@suspilnenews',
            '@svoboda_radio',
            '@talipovonline',
            '@TCH_channel',
            '@tro_zahid_zsu',
            '@truexanewsua',
            '@Tsaplienko',
            '@uawarinfographics',
            '@ukraina24tv',
            '@UkraineNow',
            '@ukrainenowenglish',
            '@ukrpravda_news',
            '@UkrzalInfo',
            '@V_Zelenskiy_official',
            '@vanek_nikolaev',
            '@VasiletsDmitriy',
            '@verkhovnaradaofukraine',
            '@vert_i_call',
            '@vidgukvolnovakha',
            '@vinnytskaODA',
            '@vklochok',
            '@vladlentatarsky',
            '@voenacher',
            '@voenkorKotenok',
            '@volynskaODA',
            '@vrogov',
            '@vysokygovorit',
            '@war_monitor',
            '@warfakes',
            '@wargonzo',
            '@waronfakesen',
            '@WarriorsUkrainian',
            '@yurasumy',
            '@zakarpatskaODA',
            '@zakharprilepin',
            '@ZE_kartel',
            '@ZeRada1',
            '@zhytomyrskaODA',
            '@zimenkin',
            '@znua_live',
            '@zoda_gov_ua'
            ]

def get_messages_from_channels(client):
    all_messages = []  # List to store message dictionaries

    for channel in channels:
        print(f"Fetching messages from channel: {channel}")
        try:
            entity = client.get_entity(channel)
            start_date = datetime(2024, 4, 1, tzinfo=utc)
            end_date = datetime(2024, 4, 30, tzinfo=utc)

            messages = client.iter_messages(entity, offset_date=end_date)
            for message in tqdm(messages, desc=f"Fetching from {channel}"):
                if message.date < start_date:
                    print(f"Message from {message.date} is outside the date range and will be skipped.")
                    break
                msg_dict = {
                    'Channel': channel,
                    'ID': message.id,
                    'Date': message.date,
                    'Text': message.text,
                    'Sender ID': message.sender_id,
                    'Sender Username': message.sender.username if message.sender else None,
                    'Media Type': message.media.__class__.__name__ if message.media else None,
                    'File Name': message.file.name if hasattr(message, 'file') and message.file else None,
                    'Mentions': [entity.user_id for entity in message.entities if hasattr(entity, 'user_id')] if message.entities else [],
                    'Forward From': message.forward.sender_id if message.forward else None,
                    'Views': message.views if hasattr(message, 'views') else None,
                    'Edit Date': message.edit_date,
                    'Hashtags': [entity.text for entity in message.entities if hasattr(entity, 'type') and entity.type == "hashtag"] if message.entities else [],
                    'Link Preview Title': message.media.webpage.title if hasattr(message.media, 'webpage') and message.media.webpage else None,
                    'Link Preview Description': message.media.webpage.description if hasattr(message.media, 'webpage') and message.media.webpage else None,
                    'Location': {'Latitude': message.geo.lat, 'Longitude': message.geo.long} if hasattr(message, 'geo') and message.geo else None,
                    'Poll Options': [option.text for option in message.media.poll.answers] if hasattr(message.media, 'poll') and message.media.poll else None
                }
                all_messages.append(msg_dict)

        except FloodWaitError as e:
            print(f"Hit rate limit, sleeping for {e.seconds}s")
            time.sleep(e.seconds)
        except Exception as e:
            print(f"An error occurred: {e}")

    return pd.DataFrame(all_messages)

def main():
    client = TelegramClient('session_name', api_id, api_hash)
    client.connect()
    
    if not client.is_user_authorized():
        print("Authorization needed. Sending code...")
        client.send_code_request(phone_number)
        client.sign_in(phone_number, input('Enter the code: '))
        print("User authorized.")
    
    df = get_messages_from_channels(client)
    print(df)

    if not df.empty:
        df.to_csv(f'C:/Users/agutierrez/Downloads/Telegram_{start_date:%Y%m%d}_{end_date:%Y%m%d}.csv', index=False, encoding='utf-8-sig')
        print("Data saved to CSV.")
    else:
        print("No data to save to CSV. 'C:/Users/agutierrez/Downloads/Telegram_{start_date:%Y%m%d}_{end_date:%Y%m%d}.csv'")

if __name__ == "__main__":
    main()
