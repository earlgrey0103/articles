
try:
    from reaper_python import *
except:
    RPR_ShowConsoleMsg('Could not load reaper python')

RPR_Undo_BeginBlock2(0)
# 功能代码片段
RPR_Undo_EndBlock2(0, 'RecArmChange', -1)

names = 'Key word:'
dvalues = ''
maxreturnlen = 10

nitems = len(dvalues.split(','))

res = RPR_GetUserInputs('Search Tracks', nitems,
        names, dvalues, maxreturnlen)

searchName = res[4].split(',')
if res[0]:
    reslen = len(searchName)
    i = 0;
    if i < reslen:
        searchName = str(searchName[i]).lower()
        i += 1

trackCount = int(RPR_CountTracks(0))
for x in range(trackCount):
    trackId = RPR_GetTrack(0, x)
    trackName = str(RPR_GetSetMediaTrackInfo_String(trackId,
         'P_Name', '', False)[3])
    RPR_SetTrackSelected(trackId, 0)

    if str(searchName) in str(trackName.lower()):
        RPR_SetTrackSelected(trackId, 1)
