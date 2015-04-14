from win32com.client import Dispatch
import time
import win32com.client

##wie = win32com.client.Dispatch('InternetExplorer.Application')
##Make IE Window Visible.
##wie.Visible = 1
## # Open this URL
##wie.Navigate('www.cnn.com')
## # Print 'Busy' while Busy.
##while wie.Busy:
## print 'Busy'
###wie.GoHome()
###wie.GoBack()
###wie.Refresh()
##wie.Quit() 


SHELL = Dispatch("Shell.Application")
wie = win32com.client.Dispatch('InternetExplorer.Application')

def get_ie(shell):
    for win in shell.Windows():
        #print win.Name
        if win.Name == "Internet Explorer":
            return win
            return None

def main(url):
    #wie = win32com.client.Dispatch('InternetExplorer.Application')
    wie.Visible = 1
    wie.Navigate(url)
    ##wie.open(url)
    time.sleep(4)
    ie = get_ie(SHELL)
    if ie:
        #print ie.LocationURL
        #print ie.LocationName 
        #print ie.ReadyState 
        #print ie 
        #print ie.Document.title 
        #print ie.Document.location 
        #print ie.Document.forms 
        ie_resp = ie.LocationName
        #wie.Quit() 

        #print ie
        return ie_resp
    else:
        print "no ie window"

    wie.Quit() 


        

if __name__ == '__main__':

    main('www.cnn.com')
    main('http://www.pg.com/en_US/')
