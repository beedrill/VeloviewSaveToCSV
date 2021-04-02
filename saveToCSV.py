'''
This is a script used in VeloView to save pcap data to CSV files
To use:
1. read pcap in Veloview
2. change the DATADIR to the directory you want, use ABSOLUTE path, make sure the folder already exist.
3. make sure the Veloview animation progress bar is at the beginning of the animation 
4. save the script.
5. in Veloview, open python console and load this script
'''
import os
DATADIR = r'C:\Users\Rusheng\Desktop\data'
vv.app.scene.GoToFirst()
while True:
    try:
        filename = os.path.join(DATADIR, str(vv.app.scene.AnimationTime) + '.csv')
        vv.saveCSVCurrentFrame(filename)
        print ('saving data on frame: ' + str(vv.getFrameFromAnimationTime(vv.app.scene.AnimationTime))) # the getFrameFromAnimationTime will return an error when reaching the end, this is how we jump out the loop
        vv.app.scene.GoToNext()
    except Exception, e:
        break
print 'done'