# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

cl = LINETCR.LINE()
cl.login(token="En7rluZ8RkDdWV8PucM0.LBlP1STnkVD4yrA8+6Cmma.9VRkYcZSi3+Hg1BXHKu7EhqjW0QAGGNWdwWvRYoQPno=")
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token="EnlSIIdybdoZdN8tIIG3.iDNe5e13vlqXbY9wdJKn0W.l5OWD53KfrQIZw0kznFQdzIShfv3YDIWmStzh8fBPNw=")
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token="EnEntHYdeNCiKb7kHOta.awZcw3GbuZLLw5TCIYckYG.UEyZsIgfp7LKoiOQle+cm3MEMhXxfvp7mR6cwV1mwoc=")
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token="EnWmnZ83AGdGBiD6zGI3.Y3mgby5SjS1Zr6O0aXyEmW.o0M3fEqct+G4U5sRrifdD19k6tl8ysxYwdHZIZhKfQo=")
ki3.loginResult()

ki4 = LINETCR.LINE()
ki4.login(token="EnlSDhbsz5uGmZH5bl50.X3YCyZzhY2mWM6Ns/a+J8a.K4q2ElC/EaviwJ6xAUb9UTkb+pY43IIVLh/97L8bBA4=")
ki4.loginResult()

ki5 = LINETCR.LINE()
ki5.login(token="EnWQ2V4DsIDQ2QWhRLNc.6Xg0KXSAW78abvdHIB/dha.lDW8oN+fBcfxgGaqSClRg//iwN5JxFPlapKVMt3bSRA=")
ki5.loginResult()

ki6 = LINETCR.LINE()
ki6.login(token="EnQdNMMNP3uPjdR5Z4pd.rvD69iN73HKYVSxvPL0Flq.JPimQhwnmv6wekkszjW16tzcPpwKW3s0qTHW4GCHQBQ=")
ki6.loginResult()

ki7 = LINETCR.LINE()
ki7.login(token="EnUQdsR9YYOKjlGTemEf.IiQITirXVeT6HGfZ+yxqZW.ReO4rVASWfvP7shMxaMrhy3QvxEKeerRpf9LRDL1G2M=")
ki7.loginResult()

ki8 = LINETCR.LINE()
ki8.login(token="EnwWwghouUjAMaqh3wHa.ogSmpRDtssvZYP+5GicW6G.vFlLIYVLPSZmKLPmZv/OF74uZD0fVvv8exgiYvtDAaM=")
ki8.loginResult()

ki9 = LINETCR.LINE()
ki9.login(token="EnnFiCZNu6FJdoShw0l1.A2StFdJX3gbgsdOS4lfsWq.cMjQ8Iy8dB2HUrDC4Swmy9g1+664CpDr3IeT7FmKVxU=")
ki9.loginResult()

print "login success "
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔═════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ 🃏🃏🃏🃏🃏
║  ♦ AFTERLOST♦
║╔════════════
║╠[1]👂 = Setlastpoint
║╠[2]👀 = Viewlastseen
║╠[3]👤 = Tag All
║╠[4]👤 @ = Mid [Tag]
║╠[5]👥 @ = Copy
║╠[6]⚽ = Open qr
║╠[7]🆗 = Close qr
║╠[8]🏃 = Keluar
║╠[9]💃 = Masuk
║╠[10]🅰 = Gname
║╠[11]👬 = Invite
║╠[12]🚯 = Kick
║╠[13]⚠ = Cek ban
║╠[14]🚫 = Ban
║╠[15]⛔ = Unban
║╠[16]🔪 = Kill ban
║╠[17]🕛 = Speed
║╠[18]👅 = Bot
║╠[19]👣 = Backup
║╠[20]🔪🔪🔪 = Attack
║╠[21]♦ @ = Kick
║║★And More★
║╚════════════
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
║ ♦BOT PROTECT♦
║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓
╚═════════════"""

Setgroup =""" 
    🃏🃏🃏🃏🃏🃏🃏🃏"""
KAC=[cl,ki,ki2,ki3,ki4,ki5,ki6,ki7,ki8,ki9]
mid = cl.getProfile().mid
kimid = ki.getProfile().mid
ki2mid = ki2.getProfile().mid
ki3mid = ki3.getProfile().mid
ki4mid = ki4.getProfile().mid
ki5mid = ki5.getProfile().mid
ki6mid = ki6.getProfile().mid
ki7mid = ki7.getProfile().mid
ki8mid = ki8.getProfile().mid
ki9mid = ki9.getProfile().mid
Bots=[mid,kimid,ki2mid]
owner = ["u95b2e9d6cb4d2af7786116bcffa70c30"]
admin = ["u95b2e9d6cb4d2af7786116bcffa70c30"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""🃏THANKS FOR ADD ME🃏""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "Protectcancel":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'copy':False,
    'target':{},
    'midsTarget':{}
    }
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile() 
backup = cl.getProfile() 
backup.dispalyName = contact.displayName 
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："] 
    for tex in tex:
      for command in commands:
        if string ==command:
          return True

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if cl.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
              	try:
                	cl.sendText(op.param1,cl.getContact(op.param2).displayName + "👏👏👏👏👏👏👏👏👏")
                	cl.kickoutFromGroup(op.param1,[op.param2])
                	X = cl.getGroup(op.param1)
                	X.preventJoinByTicket = True
                	cl.updateGroup(X)
                	cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + "👏👏👏👏👏👏👏👏👏")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "🎃🎃🎃🎃🎃🎃🎃🎃🎃")
                	random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                	X = random.choice(KAC).getGroup(op.param1)
                	X.preventJoinByTicket = True
                	random.choice(KAC).updateGroup(X)
                	random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "🎃🎃🎃🎃🎃🎃🎃🎃🎃🎃")
                	wait["blacklist"][op.param2] = True
                	f=codecs.open('st2__b.json','w','utf-8')
                	json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
        #------Protect Group 
        #>>>>>>>>>>>>>>>>>>>>>>>>>
        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = cl.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              else:
                try:
                  ki.cancelGroupInvitation(op.param1, gMembMids)
                  ki.sendText(op.param1, "🃏AFTERLOST BOT🃏\n♦Cancel Invite,Please Contact Owner & Staff")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1, "🃏PROTECT CANCEL🃏\n♦♦♦♦♦♦♦♦♦♦♦♦")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  cl.acceptGroupInvitation(op.param1)
                else:
                  cl.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
                
            if kimid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki.acceptGroupInvitation(op.param1)
                else:
                  ki.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
            
            if ki2mid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots:
                  ki2.acceptGroupInvitation(op.param1)
                else:
                  ki2.rejectGroupInvitation(op.param1)
              else:
                print "autoJoin is Off"
        #------Joined User Kick start------#
        if op.type == 17:
          if wait["Protectjoin"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                try:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kalo mau Ada yang Gabung\nJoinn on/off")
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  cl.sendText(op.param1, "Protect Join nya On Boss\nMatiin dulu kalo mau Ada yang Gabung\nJoinn on/off")
        #------Joined User Kick start------#
        if op.type == 32: #Yang Cancel Invitan langsung ke kick
          if wait["Protectcancel"] == True:
            if op.param2 not in Bots:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              elif op.param2 in owner:
                pass
              else:
                random.choice(KAC).sendText(op.param1, "🃏AFTERLOST BOT🃏\n♦Please Don't Cancel♦")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])   
        
        if op.type == 19:
          if op.param2 not in Bots:
            if op.param3 in mid:
              if op.param2 not in Bots:
                try:
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G = random.choice(KAC).getGroup(op.param1)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in kimid:
              if op.param2 not in Bots:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.001)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  
            if op.param3 in ki2mid:
              if op.param2 not in Bots:
                try:
                  G = ki.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                except:
                  G = random.choice(KAC).getGroup(op.param1) #Sanji Bertindak
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  #--------------------------------                      
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
              if wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  cl.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  cl.sendText(msg.to,"decided not to comment")
                  
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  ki.sendText(msg.to,"deleted")
                  ki2.sendText(msg.to,"deleted")
                  wait["dblack"] = False
                else:
                  wait["dblack"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  ki.sendText(msg.to,"It is not in the black list")
                  ki2.sendText(msg.to,"It is not in the black list")
                  #ki3.sendText(msg.to,"It is not in the black list")
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  cl.sendText(msg.to,"already")
                  ki.sendText(msg.to,"already")
                  ki2.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  cl.sendText(msg.to,"aded")
                  ki.sendText(msg.to,"aded")
                  ki2.sendText(msg.to,"aded")
               
              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  cl.sendText(msg.to,"deleted")
                  ki.sendText(msg.to,"deleted")
                  ki2.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False
                else:
                  wait["dblacklist"] = False
                  cl.sendText(msg.to,"It is not in the black list")
                  ki.sendText(msg.to,"It is not in the black list")
                  ki2.sendText(msg.to,"It is not in the black list")
              elif wait["contact"] == True:
                msg.contentType = 0
                cl.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                  contact = cl.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = cl.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              #if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("🅰 " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Bot2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    ki2.updateGroup(X)
                else:
                    ki2.sendText(msg.to,"It can't be used besides the group.")
            elif "🚯 " in msg.text:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Bot1 kick " in msg.text:
                midd = msg.text.replace("Bot1 kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Bot2 kick " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot2 kick ","")
                ki2.kickoutFromGroup(msg.to,[midd])
            elif "🚻 " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                ki.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Bot1 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot1 invite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Bot2 invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot2 invite ","")
                ki2.findAndAddContactsByMid(midd)
                ki2.inviteIntoGroup(msg.to,[midd])
            elif "Bot invite " in msg.text:
              #if msg.from_ in admin:
                midd = msg.text.replace("Bot invite ","")
                random.choice(KAC).findAndAddContactsByMid(midd)
                random.choice(KAC).inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin @" in msg.text:
              print "[Command]Staff add executing"
              _name = msg.text.replace("Admin add @","")
              _nametarget = _name.rstrip('  ')
              gs = cl.getGroup(msg.to)
              gs = ki.getGroup(msg.to)
              gs = ki2.getGroup(msg.to)
              targets = []
              for g in gs.members:
                if _nametarget == g.displayName:
                  targets.append(g.mid)
              if targets == []:
                random.choice(KAC).sendText(msg.to,"Contact not found")
              else:
                for target in targets:
                  try:
                    admin.append(target)
                    ki.sendText(msg.to,"🃏New Admin Add🃏")
                  except:
                    pass
                #print "[Command]Staff add executed"
              #else:
                #cl.sendText(msg.to,"Command denied.")
                #cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = ki2.getGroup(msg.to)
                #gs = k1.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ki.sendText(msg.to,"🃏Admin Remove🃏")
                        except:
                            pass
                #print "[Command]Staff remove executed"
              #else:
                #cl.sendText(msg.to,"Command denied.")
                #cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  ki.sendText(msg.to,"The stafflist is empty")
              else:
                  ki.sendText(msg.to,"🕛🕛🕛🕛")
                  mc = "||🃏AFTERLOST STAFF🃏||\n🃏🃏🃏🃏🃏🃏🃏🃏🃏\n\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  ki.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = ki2.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        ki2.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              #else:
                #cl.sendText(msg.to,"Perintah Ditolak")
                #cl.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")
                  
    #-------------=SC AllBio=----------------
            elif "Allbio:" in msg.text:
              #if msg.from_ in admin:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki2.getProfile()
                    profile.statusMessage = string
                    ki2.updateProfile(profile)
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "MyName:" in msg.text:
              #if msg.from_ in admin:
                string = msg.text.replace("MyName:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 500:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 900:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
            elif msg.text in ["All mid"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': ki2mid}
                ki2.sendMessage(msg)

                
            elif msg.text in ["Me"]:
              ##if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ki.sendMessage(msg)
            elif msg.text in ["Bot1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': kimid}
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              #if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              ##if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                
            elif msg.text in ["Cancel","cancel"]:
              ##if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"🃏No one is inviting🃏")
                        else:
                            ki.sendText(msg.to,"🃏Sorry, nobody absent🃏")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏Can not be used outside the group🃏")
                    else:
                        ki.sendText(msg.to,"🃏Not for use less than group🃏")
            elif msg.text in ["bot cancel","Bot cancel"]:
            ##if msg.from_ in admin:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["⚽","Open qr","Ourl","Open","Buka"]:
              ##if msg.from_ in admin:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n♦Qr Open♦")
                    else:
                        ki.sendText(msg.to,"🃏Already open🃏")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏Can not be used outside the group🃏")
                    else:
                        ki.sendText(msg.to,"🃏Not for use less than group🃏")
            elif msg.text in ["Luffy buka qr","Luffy open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro buka qr","Zorro open qr"]:
                if msg.toType == 2:
                    X = ki2.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Done Plak")
                    else:
                        ki2.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki2.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki2.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["🆗","Close qr","Curl","Close","Tutup"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n♦QR Close♦")
                    else:
                        cl.sendText(msg.to,"🃏Already Close🃏")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🃏Can not be used outside the group🃏")
                    else:
                        cl.sendText(msg.to,"🃏Not for use less than group🃏")
            
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Ginfo" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    cl.sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    cl.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"🃏Can not be used outside the group🃏")
                  else:
                    cl.sendText(msg.to,"🃏Not for use less than group🃏")
                
            #elif "My mid" == msg.text:
              #cl.sendText(msg.to, msg.from_)
            elif "Mid bot" == msg.text:
              ##if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,kimid)
                ki2.sendText(msg.to,ki2mid)
                
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
                ki3.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                ki2.sendMessage(msg)
            elif msg.text in ["TL: "]:
              ##if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Bot1 rename "]:
              #if msg.from_ in admin:
                string = msg.text.replace("Bot1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              #if msg.from_ in admin:
                string = msg.text.replace("Bot2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki2.getProfile()
                    profile_B.displayName = string
                    ki2.updateProfile(profile_B)
                    ki2.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              #if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                
#-------------------- Protect Mode ------------
            elif msg.text in ["💀","Mode on"]:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"💀 KICK : ON 💀")
                    else:
                        ki.sendText(msg.to,"🃏Kick Joined Group On􀜁􀇊􏿿🃏")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Udah On")
                    else:
                        ki.sendText(msg.to,"Udah On")
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"💀 Protect Invit On 💀")
                    else:
                        ki.sendText(msg.to,"Invit on")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Invit On")
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Cancel On")
                    else:
                        ki.sendText(msg.to,"Cancel on")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"💀 Protect Cancel On 💀")
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect On")
                    else:
                        ki.sendText(msg.to,"Done")
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect On")
                    else:
                        ki.sendText(msg.to,"Done")
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"💀 Protect Link On 💀")
                    else:
                        ki.sendText(msg.to,"Link On")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Protect Link On")
                    else:
                        ki.sendText(msg.to,"done")

            elif msg.text in ["👻","Mode Off"]:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👻 Kick Joined Group Off 👻")
                    else:
                        cl.sendText(msg.to,"Kick Joined Gtoup Off�")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Udah Mati")
                    else:
                        cl.sendText(msg.to,"Udah Mati")

                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👻 Protect Invite Off 👻 ")
                    else:
                        cl.sendText(msg.to,"Invite OFF")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Invite Off")
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👻 Protect Cancel Off 👻")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Cancel Off")
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👻 Block Off 👻")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👻 Block Off 👻")
                    else:
                        cl.sendText(msg.to,"done")
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"👻 Protect QR Off 👻")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
#----------------------------------------------
            elif msg.text in ["Protect on","protect on"]:
              #if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect off","protect off"]:
              #if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              #if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n♦♦♦Cancel on♦♦♦")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n♦♦♦Cancel on♦♦♦🃏")
                    else:
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              #if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n♦♦♦Cancel off♦♦♦")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Invite on","invite on"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == True:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏PROTECT ON🃏")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏PROTECT ON🃏")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              #if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏PROTECT OFF🃏")
                    else:
                        ki.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              #if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              #if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              #if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"🃏AFTERLOST BOT🃏\n ♦♦♦ Send Contact ♦♦♦")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n ♦♦♦ Send Contact ♦♦♦")
                    else:
                        ki.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              #if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n ♦♦♦ Send Contact ♦♦♦")
                    else:
                        ki.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"🃏AFTERLOST BOT🃏\n ♦♦♦ Send Contact ♦♦♦")
                    else:
                        ki.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              #if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              #if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              #if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              #if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set","Set view","Cek"]:
              #if msg.from_ in admin:
                md = "🃏AFTERLOST BOT🃏\n*♦♦♦♦♦♦♦♦♦♦♦♦♦♦*\n"
                if wait["Protectcancel"] == True: md+="[•]Protect Cancel [On]\n"
                else: md+="[•]Protect Cancel [Off]\n"
                if wait["Protectjoin"] == True: md+="[•]Protect Group [On]\n"
                else: md+="[•]Protect Group [Off]\n"
                if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
                if wait["contact"] == True: md+="[•]Contact [On]\n"
                else: md+="[•]Contact [Off]\n"
                if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="[•]Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "[•]Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="[•]Auto Leave [On]\n"
                else: md+=" Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="[•]Share [On]\n"
                else:md+="[•]Share [Off]\n"
                if wait["autoAdd"] == True: md+="[•]Auto Add [On]\n"
                else:md+="[•]Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="[•]Comment [On]\n"
                else:md+="[•]Comment [Off]\n*♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦*\n✰🃏🃏🃏🃏🃏🃏🃏🃏🃏✰\n*============*"
                ki.sendText(msg.to,md)
            elif msg.text in ["Group id","Ginfo"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              #if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              #if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              #if msg.from_ in admin:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  ki.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ki.findAndAddContactsByMid(msg.from_)
                    ki.inviteIntoGroup(gid,[msg.from_])
                  except:
                    ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              #if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki2.updateGroup(x)
                    gurl = ki2.reissueGroupTicket(msg.to)
                    ki2.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              #if msg.from_ in admin:
                if wait["clock"] == True:
                    ki.sendText(msg.to,"Bot 1 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              #if msg.from_ in admin:
                if wait["clock"] == False:
                    ki.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    ki.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
            elif "Mimic:" in msg.text:
            	if msg.from_ in admin:
            		cmd = msg.text.replace("Mimic:","")
            		if cmd == "on":
            			if mimic["status"] == False:
            				mimic["status"] = True
            				ki.sendText(msg.to,"🆗🆗🆗🆗🆗")
            			else:
            				ki.sendText(msg.to,"Mimic already on")
            		elif cmd == "off":
            			if mimic["status"] == True:
            				mimic["status"] = False
            				ki.sendText(msg.to,"🅿🅿🅿🅿🅿")
            			else:
            				ki.sendText(msg.to,"Mimic already off")
            		elif "add:" in cmd:
            			target0 = msg.text.replace("Mimic:add:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				ki.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						mimic["target"][target] = True
            						ki.sendText(msg.to,"😂😂😂😂😂")
            						#cl.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						ki.sendText(msg.to,"Failed")
            						break
            		elif "del:" in cmd:
            			target0 = msg.text.replace("Mimic:del:","")
            			target1 = target0.lstrip()
            			target2 = target1.replace("@","")
            			target3 = target2.rstrip()
            			_name = target3
            			gInfo = cl.getGroup(msg.to)
            			targets = []
            			for a in gInfo.members:
            				if _name == a.displayName:
            					targets.append(a.mid)
            			if targets == []:
            				ki.sendText(msg.to,"No targets")
            			else:
            				for target in targets:
            					try:
            						del mimic["target"][target]
            						ki.sendText(msg.to,"😭😭😭😭😭😭")
            						ki.sendMessageWithMention(msg.to,target)
            						break
            					except:
            						ki.sendText(msg.to,"Failed!")
            						break
            		elif cmd == "ListTarget":
            			if mimic["target"] == {}:
            				cl.sendText(msg.to,"No target")
                    	else:
                    		lst = "<<Lit Target>>"
                    		total = len(mimic["target"])
                    		for a in mimic["target"]:
                				if mimic["target"][a] == True:
                					stat = "On"
                				else:
                					stat = "Off"
                				lst += "\n->" + cl.getContact(mi_d).displayName + " | " + stat
                                cl.sendText(msg.to,lst + "\nTotal:" + total)
#-----------------------------------------------
            elif "Copy @" in msg.text:
            	print "Copy Sucses"
            	if msg.toType == 2:
            	    if msg.from_ in admin:
            	        _name = msg.text.replace("Copy @","")
                        _nametarget = name.rstrip(" ")
                        gs = ki.getGroup(msg.to)
                        gs = ki2.getGroup(msg.to)
                        targets = []
          
                        if _nametarget == g.displayName:
                                 targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Sukses update")
                else:
                    ki.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "👂":
              #if msg.from_ in admin:
                ki.sendText(msg.to, "🃏💀💀💀💀💀🃏")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "👀":
                 #if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        ki.sendText(msg.to, "🃏AFTERLOST BOT🃏\n\n♦Berikut Daftar Anggota yang sedang aktif♦%s\n\n\n🃏Baru saja membaca🃏\n%s\n\n🃏🃏🃏🃏\n\n🃏Suport By🃏\n♦Enemy team\n♦Afterlost team\n♦Eyes team bot\n\n\n🃏Owner Bot : Zall🃏\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        ki.sendText(msg.to, "🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["💃","Join all"]:
              #if msg.from_ in ouwner or admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki4.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki5.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki6.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki7.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki8.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        ki9.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.001)
                        H = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        H.preventJoinByTicket = True
                        cl.updateGroup(H)
                        print "Semua Sudah Lengkap"
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["🏃","Keluar","Kabur"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                  cl.getGroup(msg.to)
                  ki.leaveGroup(msg.to)
                  ki2.leaveGroup(msg.to)
                  ki3.leaveGroup(msg.to)
                  ki4.leaveGroup(msg.to)
                  ki5.leaveGroup(msg.to)
                  ki6.leaveGroup(msg.to)
                  ki7.leaveGroup(msg.to)
                  ki8.leaveGroup(msg.to)
                  ki9.leaveGroup(msg.to)
                  
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["👤","Tagall"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ki.sendMessage(msg)
                  except Exception as error:
                    print error
    #-------------Fungsi Tag All Finish---------------#
    #-------------Tag All Test------------------------#
    #-------------------------------------------------#
            elif msg.text in ["Bot Like", "Bot like"]:
              #if msg.from_ in admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["👍", "Bot like temen"]:
              #if msg.from_ in admin:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,ki2]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#   
        #------------ Copy & Backup -------------#
            elif msg.text in ["👣","backup"]:
              try:
                cl.updateDisplayPicture(backup.pictureStatus)
                cl.updateProfile(backup)
                cl.sendText(msg.to,"🕛Backup done🕛")
              except Exception as e:
                cl.sendText(msg.to, str (e))
                
            elif "👥 @" in msg.text:
              if msg.toType == 2:
                print"[Copy]"
                _name = msg.text.replace("Copy @","")
                _nametarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                targets=[]
                for g in gs.members:
                  if _nametarget == g.displayName:
                    targets.append(g.mid)
                if targets == []:
                  ki.sendText(msg.to,"Not Found")
                else:
                  for target in targets:
                    try:
                      ki.CloneContactProfile(target)
                      ki.sendText(msg.to,"🃏Success Copy🃏")
                    except Exception as e:
                      print e
        #-----------------------------------------
            elif "🔪🔪🔪" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Ready op","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    cl.sendText(msg.to,"🔪🔪🔪🔪🔪🔪🔪")
                    cl.sendText(msg.to,"🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪")
                    cl.sendText(msg.to,"🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪🔪")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': 'uc9363b5a4bfacd981c3e3c082bc4d5ef'}
                    cl.sendMessage(msg)
                    cl.sendText(msg.to,"🔪🔪🔪🔪")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots or owner:
                            if target in owner:
                              pass
                            elif target in admin:
                              pass
                            elif target in Bots:
                              pass
                            else:
                              try:
                                klist=[cl,ki,ki2]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                              except:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
        #----------------Fungsi Kick User Target Start----------------------#
            elif "♦ " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"] [0] ["M"]
                for x in key["MENTIONEES"]:
                  targets.append(x["M"])
                for target in targets:
                  try:
                    ki.kickoutFromGroup(msg.to,[target])
                  except:
                    ki.sendText(msg.to,"Error")
        #--------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              #if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes Plak")
                                except:
                                    cl.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        ki2.sendText(msg.to,"Dilarang Banned Bot")
                        #ki2.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                cl.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "👤 @" in msg.text:
              #if msg.from_ in admin:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = ki.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ki.sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        ki2.sendText(msg.to,"Tidak Ditemukan.....")
                        #ki3.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                cl.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              #if msg.from_ in admin:
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki2.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text:
              #if msg.from_ in admin:
                bctxt = msg.text.replace("Bc ","")
                a = ki.getGroupIdsJoined()
                for taf in a:
                  ki.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG"]:
              #if msg.from_ in admin:
                gids = cl.getGroupIdsJoined()
                h = ""
                for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                  cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["LG2"]:
              #if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot out","Op bye"]:
              #if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                gid = ki.getGroupIdsJoined()
                gid = ki2.getGroupIdsJoined()
                for i in gid:
                  ki.leaveGroup(i)
                  ki2.leaveGroup(i)
                if wait["lang"] == "JP":
                  cl.sendText(msg.to,"Semua Sukses Keluar Boss")
                else:
                  cl.sendText(msg.to,"He declined all invitations")
#------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Op katakan hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                #ki3.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------
            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                #ki3.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                #ki3.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                #ki3.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                #ki3.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Welcome"]:
                ki.sendText(msg.to,"Selamat datang di Group Kami")
                ki.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif "/Copy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("/Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    ki.cloneContactProfile(target)
                                    ki.sendText(msg.to, "👻👻👻👻👻👻")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                ki2.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                #ki3.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["👅","Absen bot","Absen dulu","Respon"]:
              #if msg.from_ in admin
                ki.sendText(msg.to,"🃏")
                ki2.sendText(msg.to,"🃏")
                ki3.sendText(msg.to,"🃏")
                ki4.sendText(msg.to,"🃏")
                ki5.sendText(msg.to,"🃏")
                ki6.sendText(msg.to,"🃏")
                ki7.sendText(msg.to,"🃏")
                ki8.sendText(msg.to,"🃏")
                ki9.sendText(msg.to,"🃏")
      #-------------Fungsi Respon Finish---------------------#
                            

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","🕛"]:
              #if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "Menghitung Kecepatan...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["🚫"]:
              #if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"⚠⚠⚠⚠⚠")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["⛔"]:
              #if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"🚫🚫🚫🚫🚫")
                #ki.sendText(msg.to,"Kirim contact")
                #kk.sendText(msg.to,"Kirim contact")
                #kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Bot"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': mid}
              ki.sendText(msg.to,"🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏")
              ki.sendMessage(msg)
              ki.sendText(msg.to,"🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏")
              ki.sendText(msg.to,"🃏AFTERLOST BOT🃏")
                
      #-------------Fungsi Chat ----------
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["⚠"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["🔪"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              #if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          ki.sendText(op.param1, "🃏AFTERLOSTBOT🃏\n🃏Selamat Datang Di Grup  " + ">>>" + str(ginfo.name) + "<<<" + "\n" + "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName + "\n\n" + "Budayakan Baca Note 😊\nSemoga Betah 🃏")
          #cl.sendText(op.param1, "Founder Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
          #cl.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
          #print "MEMBER HAS JOIN THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,200):
      hasil = cl.activity(limit=200)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by 🃏zall🃏👈\n")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"🃏like🃏")
          ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki2.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏🃏")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.01)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,200):
        hasil = cl.activity(limit=200)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki2.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by 🃏zall🃏")
                    ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"🃏🃏🃏🃏🃏")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
