# uncompyle6 version 3.5.0
# Python bytecode 3.7 (3394)
# Decompiled from: Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
# [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)]
# Embedded file name: C:/Users/Om/Documents/maya/2022/scripts\as_SmoothNearestMain.py
# Size of source mod 2**32: 17413 bytes
import maya.cmds as mc
import maya.mel as mel
import re, sys, os, socket, webbrowser as web
from uuid import getnode
import pymel.core as pm

class as_SmoothNearestMain:

    def __init__(self):
        """
                Its a advance feature of HyperSkinning System..
                                
                **as_SmoothNearestMain_v2.0**
                
                About :         
                -------
                Author: (Subbaiah) Subbu Addanki
                Character Supervisor (Rigging) & Programmer
                
                Visit :
                -------
                http://www.pythonscripting.com  
                http://subbuadd.blogspot.com
                
                Contact :
                ---------                               
                Mail Id: subbu.add@gmail.com    
                Mobile No: +91-8466086325
                
                Copyright (c) as_SmoothNearestMain :
                ------------------------------------            
                ** (Subbaiah) Subbu Addanki. All Rights Reserved. **
                
                Compiled Only For:
                ------------------              
                ** Only For CreativeCrash **
                """
        _limit2Ver = [
         2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023]
        _checkMayaVersion = 1
        if _checkMayaVersion:
            if self._mayaVer() in _limit2Ver:
                pass
            else:
                limit2Ver = list(map(str, _limit2Ver))
                limit2VerStr = ', '.join(limit2Ver)
                self._as_SmoothNearestMain__confirmAction('This tool is compiled only for Maya {}!!'.format(limit2VerStr))
                raise RuntimeError('This tool is compiled only for Maya {}!!'.format(limit2VerStr))
            inTime = True
            if not inTime:
                web.open('http://www.creativecrash.com/maya/script/as_smoothnearest-a-magic-in-hyper-skinning-system')
                web.open('http://www.pythonscripting.com/store/')
                errorMsg = "Free Trail version was expired.. \nDownload again\nNot Working after re-download again ??\nDon't worry. It will be updated soon !!"
                errorMsg += '\n\nIf you need unlimited version right now for Free??  Reach me at : subbu.add@gmail.com for unlimited version !!'
                self._confirmAction(errorMsg)

            def getNetworkIp():
                ipAddress = None
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    s.connect(('www.gmail.com', 0))
                    ipAddress = s.getsockname()[0]
                except:
                    pass

                return ipAddress

            ipAddress = getNetworkIp()

            def get_MacAddress(host='localhost'):
                """ Returns the MAC address of a network host, requires >= WIN2K."""
                import ctypes, socket, struct
                try:
                    SendARP = ctypes.windll.Iphlpapi.SendARP
                except:
                    return
                    if host == '127.0.0.1' or host.lower() == 'localhost':
                        host = socket.gethostname()
                    try:
                        inetaddr = ctypes.windll.wsock32.inet_addr(host)
                        if inetaddr in (0, -1):
                            raise Exception
                    except:
                        hostip = socket.gethostbyname(host)
                        inetaddr = ctypes.windll.wsock32.inet_addr(hostip)

                    buffer = ctypes.c_buffer(6)
                    addlen = ctypes.c_ulong(ctypes.sizeof(buffer))
                    if SendARP(inetaddr, 0, ctypes.byref(buffer), ctypes.byref(addlen)) != 0:
                        return
                    macaddr = ''
                    for intval in struct.unpack('BBBBBB', buffer):
                        if intval > 15:
                            replacestr = '0x'
                        else:
                            replacestr = 'x'
                        if macaddr != '':
                            macaddr = ':'.join([macaddr, hex(intval).replace(replacestr, '')])
                        else:
                            macaddr = ''.join([macaddr, hex(intval).replace(replacestr, '')])

                    macId = macaddr.upper()
                    if macId == '00:00:00:00:00:00':
                        return
                    return macId

            def getMacAddress():
                import platform as pf
                macId = None
                if sys.platform == 'win32' or pf.system() == 'Windows':
                    for line in os.popen('ipconfig /all'):
                        if line.lstrip().startswith('Physical Address'):
                            macId = line.split(':')[1].strip().upper()
                            break
                        else:
                            for line in os.popen('/sbin/ifconfig'):
                                if line.find('Ether') > -1:
                                    macId = line.split()[4].strip()
                                    break

                elif sys.platform in ('linux', 'linux2') or pf.system() == 'Linux':
                    try:
                        import LinuxMac
                        macId = LinuxMac.get_mac_address()
                    except:
                        pass

                    return macId

            macId = getMacAddress() or get_MacAddress()
            givenMacId = '3003c844c689'
            currentMacId = macId or getnode()
            checkMacId = 0
            checkMacId = 0
            if checkMacId:
                pass
        if getnode() == '167739360081L' or getnode() == '238276881964104L':
            pass
        elif not getnode() == '167739360081L':
            if not getnode() == '238276881964104L':
                if getnode() == '228800471355458L':
                    pass
        elif not macId == '3003c844c689':
            if macId == '64:51:06:42:21:31':
                pass
        if not getnode() == '176831338761811L':
            pass
            

    def message(self, messageTxt):
        """
                Sends a given message through confirmDialog window
                """
        confirmDialog(title='Message ..!', message=messageTxt, button=['Yes'], defaultButton='Yes')

    def sortByDict(self, dictName, sortType='up', returnType='keys', sortListIndex=0, sliceDict=None, **shNames):
        """
                eRig.sortedByDict({'j1':10, 'j2':2, 'j3':-1.0, 'j4':50.0, 'j5':0, 'j6':10}, 'up')
                sliceDict : None | ['>', val] | ['<', val] | ['>=', val] | ['<=', val] | ['==', val]
                """
        if shNames:
            dictName = shNames['n'] if 'n' in shNames else dictName
            sortType = shNames['st'] if 'st' in shNames else sortType
            returnType = shNames['rt'] if 'rt' in shNames else returnType
            sortListIndex = shNames['sli'] if 'sli' in shNames else sortListIndex
            sliceDict = shNames['si'] if 'si' in shNames else sliceDict
        if type(dictName) != dict:
            raise RuntimeError('"%s" is not dictionary ..!' % str(dictName))
        if sliceDict:
            if sliceDict[0] == '>':
                dictName = dict([(k, v) for k, v in list(dictName.items()) if dictName[k][sortListIndex] > sliceDict[1]])
            elif sliceDict[0] == '>=':
                dictName = dict([(k, v) for k, v in list(dictName.items()) if dictName[k][sortListIndex] >= sliceDict[1]])
            elif sliceDict[0] == '<':
                dictName = dict([(k, v) for k, v in list(dictName.items()) if dictName[k][sortListIndex] < sliceDict[1]])
        if sliceDict[0] == '<=':
            dictName = dict([(k, v) for k, v in list(dictName.items()) if dictName[k][sortListIndex] <= sliceDict[1]])
        elif sliceDict[0] == '==':
            dictName = dict([(k, v) for k, v in list(dictName.items()) if dictName[k][sortListIndex] == sliceDict[1]])
        else:
            valList = list(dictName.values())
            shiftToKeys = False
            for val in valList:
                if not type(val) == int:
                    if not type(val) == float:
                        if type(val) == list:
                            continue
                        else:
                            shiftToKeys = True
                            break

            if shiftToKeys:
                valList = list(dictName.keys())
                for val in valList:
                    if not type(val) == int:
                        if not type(val) == float:
                            if type(val) == list:
                                continue
                            else:
                                raise RuntimeError('"%s" is neither "int" nor "float" value ..!' % str(val))

            if all([type(x) == list for x in valList]):
                valList = sorted(valList, key=(itemgetter(sortListIndex)))
            else:
                valList.sort()
            if sortType.lower() == 'down' or sortType.lower() == 'dn':
                valList.reverse()

        if returnType == 'keys':
            keyList = []
            for val in valList:
                for keyName in list(dictName.keys()):
                    if val == dictName[keyName] and keyName not in keyList and type(keyName) == str:
                        if objExists(keyName):
                            keyName = asNode(keyName)
                        keyList.append(keyName)
                        break

            return keyList
        if returnType == 'values':
            return valList

    def getSkinWeights(self, vtxName, skinClust):
        valList = skinPercent(skinClust, vtxName, q=1, v=1)
        infList = mc.skinCluster((str(skinClust)), q=1, inf=1)
        skinValDict = dict(list(zip(infList, valList)))
        skinValDict = dict([val for val in list(skinValDict.items()) if val[1] > 0.0])
        return skinValDict

    def restrictedZone_FreeTool(self):
        web.open('http://www.pythonscripting.com/')
        restrictedMsg = 'Oops ..!!\nThis option is not available | Limited to 100 Vertices In Free Version !!\n\n'
        restrictedMsg += 'Visit "http://www.pythonscripting.com/" For Latest Updates !!'
        HyperSkin._as_SmoothNearestMain__confirmAction(restrictedMsg)

    def limitInfs_skinClust(self, limitInfs=5, skinClust=None, limitVtx=False):
        vtxList = mc.filterExpand(sm=31)
        if limitVtx:
            if len(vtxList) >= 100:
                web.open('http://www.creativecrash.com/maya/script/as_smoothnearest-a-magic-in-hyper-skinning-system')
                self.restrictedZone_FreeTool()
                self._confirmAction(errorMsg)
            if not skinClust:
                vtxMesh = vtxList[0].split('.')[0]
                skinClust = str(pm.listHistory(vtxMesh, type='skinCluster')[0])
            allInfs = pm.skinCluster(skinClust, q=1, inf=1)
            for vtx in vtxList:
                wDict = self.getSkinWeights(vtx, skinClust)
                wJnts = self.sortByDict(wDict)
                wJnts.reverse()
                limitedJnts = wJnts[0:limitInfs]
                for jnt in limitedJnts:
                    mc.setAttr(jnt + '.liw', 0)

                for jnt in allInfs:
                    if jnt not in limitedJnts:
                        mc.setAttr(jnt + '.liw', 1)

                for jnt in wJnts[limitInfs:]:
                    pm.skinPercent(skinClust, vtx, tv=[jnt, 0])

    def as_SmoothNearest(self, limitInfs=0):
        vtxList = mc.filterExpand(sm=31)
        if vtxList:
            mel.eval('doSmoothSkinWeightsArgList 3 {"0.0001", "5", "0", "0"}')
            mel.eval('GrowPolygonSelectionRegion()')
            mc.select((list(set(mc.filterExpand(sm=31)) ^ set(vtxList))), r=1)
            mel.eval('doSmoothSkinWeightsArgList 3 {"0.0001", "5", "0", "0"}')
            if limitInfs:
                self.limitInfs_skinClust(limitInfs)

    def _mayaVer(self):
        mayaStr = str(mc.about(v=1))
        first4 = mayaStr[0:4]
        if len(first4) >= 4:
            pass
        if first4.isalnum():
            if first4.startswith('20'):
                return int(first4)
            return
        else:
            return

    def __confirmAction(self, action):
        confirmDialog(title='Warning..', bgc=(1, 0.5, 0), message=action, button=['Yes'], defaultButton='Yes')
        try:
            sysFile((internalVar(usd=1) + 'as_SmoothNearestMain.pyc'), delete=True)
        except:
            pass

        raise RuntimeError(action)

    def _isInTime(self, startDate=[
 2017, 1, 1], endDate=[2018, 1, 1], onlineTime=1, showDaysLeft=1):
        import datetime as dt
        currentDate = None
        if onlineTime:
            try:
                import urllib.request, urllib.parse, urllib.error
                link = 'http://just-the-time.appspot.com/'
                f = urllib.request.urlopen(link)
                currentDate = f.read()[0:10]
            except:
                web.open('http://www.pythonscripting.com/store/2016/4/2/05-ashyperskin')
                errorMsg = 'Oops..!! \nCheck For Internet Connection .. !!\n'
                errorMsg += '\n\nIf you need unlimited version right now ?  Please contact at : subbu.add@gmail.com for more details !!'
                self._as_SmoothNearestMain__confirmAction(errorMsg)
                return False

        else:
            try:
                currentDate = str(dt.date.today())
            except:
                web.open('http://www.pythonscripting.com/store/2016/4/2/05-ashyperskin')
                errorMsg = 'Free Limited Trail Version Of AHSS Was Expired.. !!\n'
                errorMsg += "\nDownload again\nNot Working after re-download ??\nDon't worry. It might be updated soon !!"
                errorMsg += '\n\nIf you need unlimited version right now ?  Please contact at : subbu.add@gmail.com for more details !!'
                self._as_SmoothNearestMain__confirmAction(errorMsg)
                return False
            else:
                if showDaysLeft:
                    if currentDate:
                        cDate = [int(num) for num in currentDate.split('-')]
                        d0 = dt.date(cDate[0], cDate[1], cDate[2])
                        d1 = dt.date(endDate[0], endDate[1], endDate[2])
                        delta = d1 - d0
                        daysLeft = delta.days - 1
                        if daysLeft > 0:
                            self.message('No Of Days Left To Utilize Free AHSS \n                   ** {} **'.format(daysLeft))
                        else:
                            web.open('http://www.pythonscripting.com/store/2016/4/2/05-ashyperskin')
                            errorMsg = 'Oops..!! \nCheck For Internet Connection .. !!\n'
                            errorMsg += '\n\nIf you need unlimited version right now ?  Please reach me at : subbu.add@gmail.com for more details !!'
                            self._as_SmoothNearestMain__confirmAction(errorMsg)
                            return False
                    reObj = re.compile('(?P<Year>[\\d]{4})-(?P<Month>[\\d]{1,2})-(?P<Day>[\\d]{1,2})')
                    testObj = reObj.match(currentDate)
                    yearCheck = int(testObj.group('Year'))
                    monthCheck = int(testObj.group('Month'))
                    dayCheck = int(testObj.group('Day'))
                    startYear = startDate[0]
                    startMonth = startDate[1]
                    startDay = startDate[2]
                    endYear = endDate[0]
                    endMonth = endDate[1]
                    endDay = endDate[2]
                    if yearCheck >= endYear:
                        pass
                    if monthCheck >= endMonth or yearCheck > endYear:
                        if dayCheck >= endDay or monthCheck > endMonth:
                            web.open('http://www.pythonscripting.com/store/2016/4/2/05-ashyperskin')
                            errorMsg = 'Free Limited Trail Version Of AHSS Was Expired.. !!\n'
                            errorMsg += "\nDownload again\nNot Working after re-download ??\nDon't worry. It will be updated soon !!"
                            errorMsg += '\n\nIf you need unlimited version right now ?  Please reach me at : subbu.add@gmail.com for more details !!'
                            self._as_SmoothNearestMain__confirmAction(errorMsg)
                            return False
                        if yearCheck <= startYear:
                            pass
                if monthCheck <= startMonth or yearCheck < startYear:
                    if dayCheck <= startDay or monthCheck < startMonth:
                        web.open('http://www.pythonscripting.com/store/2016/4/2/05-ashyperskin')
                        errorMsg = 'Free Limited Trail Version Of AHSS Was Expired.. !!\n'
                        errorMsg += "\nDownload again\nNot Working after re-download ??\nDon't worry. It will be updated soon !!"
                        errorMsg += '\n\nIf you need unlimited version right now ?  Please reach me at : subbu.add@gmail.com for more details !!'
                        self._as_SmoothNearestMain__confirmAction(errorMsg)
                        return False
                    else:
                        return True

    def _limit2Week(self):
        import datetime as dt
        kissMe = str(dt.date.today())
        reObj = re.compile('(?P<Big>[\\d]{4})-(?P<Mid>[\\d]{1,2})-(?P<Small>[\\d]{1,2})')
        testObj = reObj.match(kissMe)
        yearCheck = int(testObj.group('Big'))
        monthCheck = int(testObj.group('Mid'))
        dayCheck = int(testObj.group('Small'))
        lastDay = 3
        lastMonth = 3
        lastYear = 2016
        nextDay = 26
        nextMonth = 4
        nextYear = 2016
        if yearCheck >= nextYear:
            pass
        if monthCheck >= nextMonth or yearCheck > nextYear:
            if dayCheck >= nextDay or monthCheck > nextMonth:
                pass
            return False
        else:
            if yearCheck <= lastYear:
                if monthCheck <= lastMonth or yearCheck < lastYear:
                    pass
            if dayCheck <= lastDay or monthCheck < lastMonth:
                return False
            return True

    def _confirmAction(self, action):
        mc.confirmDialog(title='Warning..', bgc=(1, 0.5, 0), message=action, button=['Yes'], defaultButton='Yes')
        try:
            mc.sysFile((internalVar(usd=1) + 'as_SmoothNearestMain.pyc'), delete=True)
        except:
            pass

        # raise RuntimeError(action)

    def confirmAction(self, action, raiseErr=False):
        """
                Requests User to confirm an action shown in confirmDialog window
                """
        if raiseErr:
            mc.confirmDialog(title='Warning..', bgc=(1, 0.5, 0), message=action, button=['Yes'], defaultButton='Yes')
            raise RuntimeError(action)
        confirm = mc.confirmDialog(title='Confirm Action?', message=action, button=['Yes', 'No'], defaultButton='Yes', cancelButton='No', dismissString='No')
        if confirm == 'Yes':
            return True
        else:
            return False


SmoothNearest = as_SmoothNearestMain()
SmoothNearest.as_SmoothNearest()
