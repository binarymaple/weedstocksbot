# apt update
# apt upgrade
# apt install python-pip
# : setup your systemd to run the script 
# systemctl start/stop/restart/status weedstocksbot.service
# pip install praw (note written with version 3.6.0)
# pip install lxml

import praw
import time
from lxml import html
from lxml import etree
import requests
import datetime

sub = "weedstocks"

r = praw.Reddit('Weed Stocks Ticker Agent 1.0 by /u/binarymaple')
r.set_oauth_app_info(client_id='REDACTED_FOR_SECURITY', client_secret='REDACTED_FOR_SECURITY', redirect_uri='http://127.0.0.1:65010/authorize_callback')
r.refresh_access_information('REDACTED_FOR_SECURITY')

r.send_message('binarymaple', 'Weed Stocks Ticker Agent is Online', 'This is an automated message.')

oldtime = time.time()

checkSSL = True

while True:
    try:
        if time.time() - oldtime > 1800: # it's been 30 minutes
            r.refresh_access_information('REDACTED_FOR_SECURITY')
            oldtime = time.time() # reset the clock
        d = datetime.datetime.now() 
        if d.isoweekday() in range(1, 6) and d.hour in range(9, 17):
            page = requests.get('https://ca.finance.yahoo.com/q?s=CGC.TO&ql=1', verify=checkSSL)
            tree = html.fromstring(page.content)
            CGC_price = tree.xpath('//span[@id="yfs_l84_cgc.to"]/text()')
            CGC_price = float(CGC_price[0])
            CGC_change = tree.xpath('//span[@id="yfs_c63_cgc.to"]/text()')
            CGC_change = float(CGC_change[0])
            CGC_percent = tree.xpath('//span[@id="yfs_p43_cgc.to"]/text()')
            CGC_percent = CGC_percent[0]
            CGC_percent = float(CGC_percent[CGC_percent.find("(")+1:CGC_percent.find("%")])
            for elem in tree.xpath("//span[@id='yfs_c63_cgc.to']"):
                CGC_inner_html = etree.tostring(elem, pretty_print=True)
            if 'Down' in CGC_inner_html:
                CGC_change = -CGC_change
                CGC_percent = -CGC_percent
            page = requests.get('https://ca.finance.yahoo.com/q?s=APH.V&ql=1', verify=checkSSL)
            tree = html.fromstring(page.content)
            APH_price = tree.xpath('//span[@id="yfs_l84_aph.v"]/text()')
            APH_price = float(APH_price[0])
            APH_change = tree.xpath('//span[@id="yfs_c63_aph.v"]/text()')
            APH_change = float(APH_change[0])
            APH_percent = tree.xpath('//span[@id="yfs_p43_aph.v"]/text()')
            APH_percent = APH_percent[0]
            APH_percent = float(APH_percent[APH_percent.find("(")+1:APH_percent.find("%")])
            for elem in tree.xpath("//span[@id='yfs_c63_aph.v']"):
                APH_inner_html = etree.tostring(elem, pretty_print=True)
            if 'Down' in APH_inner_html:
                APH_change = -APH_change
                APH_percent = -APH_percent
            page = requests.get('https://ca.finance.yahoo.com/q?s=OGI.V&ql=1', verify=checkSSL)
            tree = html.fromstring(page.content)
            OGI_price = tree.xpath('//span[@id="yfs_l84_ogi.v"]/text()')
            OGI_price = float(OGI_price[0])
            OGI_change = tree.xpath('//span[@id="yfs_c63_ogi.v"]/text()')
            OGI_change = float(OGI_change[0])
            OGI_percent = tree.xpath('//span[@id="yfs_p43_ogi.v"]/text()')
            OGI_percent = OGI_percent[0]
            OGI_percent = float(OGI_percent[OGI_percent.find("(")+1:OGI_percent.find("%")])
            for elem in tree.xpath("//span[@id='yfs_c63_ogi.v']"):
                OGI_inner_html = etree.tostring(elem, pretty_print=True)
            if 'Down' in OGI_inner_html:
                OGI_change = -OGI_change
                OGI_percent = -OGI_percent
            page = requests.get('https://ca.finance.yahoo.com/q?s=MT.V&ql=1', verify=checkSSL)
            tree = html.fromstring(page.content)
            MT_price = tree.xpath('//span[@id="yfs_l84_mt.v"]/text()')
            MT_price = float(MT_price[0])
            MT_change = tree.xpath('//span[@id="yfs_c63_mt.v"]/text()')
            MT_change = float(MT_change[0])
            MT_percent = tree.xpath('//span[@id="yfs_p43_mt.v"]/text()')
            MT_percent = MT_percent[0]
            MT_percent = float(MT_percent[MT_percent.find("(")+1:MT_percent.find("%")])
            for elem in tree.xpath("//span[@id='yfs_c63_mt.v']"):
                MT_inner_html = etree.tostring(elem, pretty_print=True)
            if 'Down' in MT_inner_html:
                MT_change = -MT_change
                MT_percent = -MT_percent
            page = requests.get('https://ca.finance.yahoo.com/q?s=ACB.V&ql=1', verify=checkSSL)
            tree = html.fromstring(page.content)
            ACB_price = tree.xpath('//span[@id="yfs_l84_acb.v"]/text()')
            ACB_price = float(ACB_price[0])
            ACB_change = tree.xpath('//span[@id="yfs_c63_acb.v"]/text()')
            ACB_change = float(ACB_change[0])
            ACB_percent = tree.xpath('//span[@id="yfs_p43_acb.v"]/text()')
            ACB_percent = ACB_percent[0]
            ACB_percent = float(ACB_percent[ACB_percent.find("(")+1:ACB_percent.find("%")])
            for elem in tree.xpath("//span[@id='yfs_c63_acb.v']"):
                ACB_inner_html = etree.tostring(elem, pretty_print=True)
            if 'Down' in ACB_inner_html:
                ACB_change = -ACB_change
                ACB_percent = -ACB_percent
            TickerTime = tree.xpath('//span[@id="yfs_t53_acb.v"]/text()')
            TickerTime = TickerTime[0]
            if CGC_percent < 0:
                CGC_color = '(/red)'
            elif CGC_percent == 0:
                CGC_color = '(/black)'
            else:
                CGC_color = '(/green)'
            if APH_percent < 0:
                APH_color = '(/red)'
            elif APH_percent == 0:
                APH_color = '(/black)'
            else:
                APH_color = '(/green)'
            if OGI_percent < 0:
                OGI_color = '(/red)'
            elif OGI_percent == 0:
                OGI_color = '(/black)'
            else:
                OGI_color = '(/green)'
            if MT_percent < 0:
                MT_color = '(/red)'
            elif MT_percent == 0:
                MT_color = '(/black)'
            else:
                MT_color = '(/green)'
            if ACB_percent < 0:
                ACB_color = '(/red)'
            elif ACB_percent == 0:
                ACB_color = '(/black)'
            else:
                ACB_color = '(/green)'
            CGC_price = '{0:.02f}'.format(CGC_price)
            CGC_change = '{0:+.02f}'.format(CGC_change)
            CGC_percent = '{0:+.02f}'.format(CGC_percent)
            APH_price = '{0:.02f}'.format(APH_price)
            APH_change = '{0:+.02f}'.format(APH_change)
            APH_percent = '{0:+.02f}'.format(APH_percent)
            OGI_price = '{0:.02f}'.format(OGI_price)
            OGI_change = '{0:+.02f}'.format(OGI_change)
            OGI_percent = '{0:+.02f}'.format(OGI_percent) 
            MT_price = '{0:.02f}'.format(MT_price)
            MT_change = '{0:+.02f}'.format(MT_change)
            MT_percent = '{0:+.02f}'.format(MT_percent)
            ACB_price = '{0:.02f}'.format(ACB_price)
            ACB_change = '{0:+.02f}'.format(ACB_change)
            ACB_percent = '{0:+.02f}'.format(ACB_percent)
            settings = r.get_settings(sub)
            sidebar_contents = settings['description']
            pre_sidebar_contents = sidebar_contents.split('**Ticker** | **Price** | **Change ($)** | **Change (%)**')
            post_sidebar_contents = sidebar_contents.split('Please contact /u/binarymaple to report any problems.)*')
            pre_sidebar_contents = pre_sidebar_contents[0]
            post_sidebar_contents = post_sidebar_contents[1]
            stock_table = '\n\n**Ticker** | **Price** | **Change ($)** | **Change (%)**\n:--------|:--------:|:--------:|:---------:\n**CGC** | ' + CGC_price + ' | ' + CGC_change + '| [' + CGC_percent +']' + CGC_color + '\n**APH** | ' + APH_price + ' | ' + APH_change + '| [' + APH_percent +']' + APH_color + '\n**OGI** | ' + OGI_price + ' | ' + OGI_change + '| [' + OGI_percent +']' + OGI_color + '\n**MT** | ' + MT_price + ' | ' + MT_change + '| [' + MT_percent +']' + MT_color + '\n**ACB** | ' + ACB_price + ' | ' + ACB_change + '| [' + ACB_percent +']' + ACB_color + '\n\n\n*^(BETA ticker information is NOT guaranteed to be accurate, delayed 15 minutes and updated every 5 minutes. Last updated ' + TickerTime + '. Please contact /u/binarymaple to report any problems.)*'
            sidebar_contents = pre_sidebar_contents
            sidebar_contents += stock_table
            sidebar_contents += post_sidebar_contents
            r.edit_wiki_page(sub, 'config/sidebar', sidebar_contents)
    except:
        r.send_message('binarymaple', 'Weed Stocks Ticker Agent Broke', 'This is an automated message.')
        time.sleep(60) # sleep an extra 60 seconds
    time.sleep(300) # sleep 5 minutes
