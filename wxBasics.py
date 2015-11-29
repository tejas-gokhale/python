import wx   # allows us to use wx
class chappy(wx.Frame):
    # Frame is a class in wx, allows us to use frames in wx
    # now init constructor function
    # coz we want a double-click and boom
    # wham-bam thakn you ma'am
    
    # constructor method allows the frame to automatically popup
    def __init__(self, parent, id): #__init__ is the first thing that happens
        wx.Frame.__init__(self, parent, id, 'Frame aka Window', size = (300, 400)) # this is the title of the window
        panel = wx.Panel(self)      # panel created
    
        # status bar (pixel info, etc)
        # -----------------------------
        status = self.CreateStatusBar()
        
        # menu bar
        # -------------------
        menubar = wx.MenuBar()
        first = wx.Menu()
        second = wx.Menu()
        # add items to the menu
        first.Append(wx.NewId(), "New Window", "This is a new window")
        first.Append(wx.NewId(), "Open", "open up bitch")
        # add these menus to the menubar
        menubar.Append(first, "File")
        menubar.Append(second, "Bleh")
        self.SetMenuBar(menubar)    #sets the menubar on the screen
        
        # user input
        # -------------------
        # Yes or No, or OK (wx.YES_NO, wx.OK)
        box = wx.MessageDialog(None, 'Do I got swag?', 'Question 1', wx.YES_NO)
        answer = box.ShowModal()    # the value of YES or NO as int
        box.Destroy()
        
        # ... text input from user
        boxText = wx.TextEntryDialog(None, "What's your name?", "Name", "default text")
        if boxText.ShowModal() == wx.ID_OK:
            ans = boxText.GetValue()
        else:
            print "You hit Cancel"
        boxText.Destroy()
        
        # ... choice dialog
        boxChoice = wx.SingleChoiceDialog(None, 'What\'s your favorite food?', 'Food Question', ['Fish', 'Beef', 'Potato', 'Bread'])
        if boxChoice.ShowModal() == wx.ID_OK:
            choice = boxChoice.GetStringSelection()
        else:
            print "You hit Cancel"
        boxChoice.Destroy()
        
        # static text
        # -----------------
        wx.StaticText(panel, -1, "Tejas introduces you to Static Text", (10, 10)) #position of static text
        custom = wx.StaticText(panel, -1, "%s's fav food is %s" % (ans, choice), (10, 40), (260, -1), wx.ALIGN_CENTER) #length of static text, -1= height of text
        custom.SetForegroundColour('yellow')
        custom.SetBackgroundColour('blue')
        
        # slider
        # ----------------------
        slider = wx.Slider(panel, -1, 50, 1, 100, pos = (10, 70), size = (250, -1), style = wx.SL_AUTOTICKS | wx.SL_LABELS) # (parent, id, default, min, max, pos, size, style)
        slider.SetTickFreq(5, 1)    # ticks are 5 numbers apart
        
        # spinners
        # ----------------------
        spinner = wx.SpinCtrl(panel, -1, "", (50, 180),(40, -1))
        #to set the range
        spinner.SetRange(1, 100)
        spinner.SetValue(10)
        #for wrap-around set style to SP_WRAP
        
        # checkbox
        # --------------------
        wx.CheckBox(panel, -1, "Apples", (180, 170), (90, -1))
        wx.CheckBox(panel, -1, "Tuna", (180, 190), (90, -1))
        wx.CheckBox(panel, -1, "Beef", (180, 210), (90, -1))
        
        # listbox (dropdown)
        # --------------------
        mylist = ['USA', 'UK', 'India', 'Russia', 'China']
        container = wx.ListBox(panel, -1, (130, 260), (90, 40), mylist, wx.LB_SINGLE)
        container.SetSelection(2) # default default selection
        
        # button
        # --------------------
        button = wx.Button(panel, label = "Exit", pos = (80, 120), size = (40, 40))   # parent is panel, so button is inside panel
        # now bind an event to a button or action
        # what is the event? clicking the button
        # what's the action? closing the button
        self.Bind(wx.EVT_BUTTON, self.closebutton, button)
        self.Bind(wx.EVT_CLOSE, self.closewindow)
        
        # ... button with images
        pic = wx.Image("C:\Users\Tejas\Pictures\sign.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.picButton = wx.BitmapButton(panel, -1, pic, pos = (180, 120), size = (40, 40))
        self.Bind(wx.EVT_BUTTON, self.closebutton, self.picButton)
        self.picButton.SetDefault()


    def closebutton(self, event):
        self.Close(True)
    
    def closewindow(self, event):
        self.Destroy()
        
    # if we run this program right now, nothing will show up
    # because we didn't write code for "show window"
        

# every wxPython application needs two things: application object and frame object (inner workings and display)
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = chappy(parent = None, id = -1)
    frame.Show()        
    app.MainLoop()
    
    names = ['chappy', 'annie', 'bhusa', 'gela', 'bhogya']
    singleChoice = wx.SingleChoiceDialog(None, "Confirm your name", "Name Check", names)
    if singleChoice.ShowModal() == wx.ID_OK:
        print "Thank you %s\n" % singleChoice.GetStringSelection()
    singleChoice.Destroy()

    
    
    
