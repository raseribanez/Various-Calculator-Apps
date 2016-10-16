# Ben Woodfield
# A Simple Calculator program - NEEDS GTK MODULE

import gtk

class MainWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.connect('destroy',gtk.main_quit)
        self.set_title('Calculator')
        self.set_size_request(320,240)
        self.set_position(gtk.WIN_POS_CENTER)

        self.set_border_width(10)

        self.num1 = '0'
        self.num2 = '0'

        self.operator = '+'

        vbox = gtk.VBox()

        hbox1 = gtk.HBox()
        hbox2 = gtk.HBox()
        hbox3 = gtk.HBox()
        hbox4 = gtk.HBox()
        hbox5 = gtk.HBox()
        hbox6 = gtk.HBox()

        self.table = gtk.Table(5,4,True)

        btn_cls  = gtk.Button('Cls')
        btn_exit = gtk.Button('Exit')

        btn_cls.connect('clicked',self.clrscr)
        btn_exit.connect('clicked',gtk.main_quit)
        
        btn_zero = gtk.Button('0')
        btn_one = gtk.Button('1')
        btn_two = gtk.Button('2')
        btn_three = gtk.Button('3')
        btn_four = gtk.Button('4')
        btn_five = gtk.Button('5')
        btn_six  = gtk.Button('6')
        btn_seven = gtk.Button('7')
        btn_eight = gtk.Button('8')
        btn_nine = gtk.Button('9')
        btn_point = gtk.Button('.')

        numbuttons = [btn_zero,btn_one,btn_two,btn_three,btn_four,\
                   btn_five,btn_six,btn_seven,btn_eight,btn_nine]

        count = -1
        
        for button in numbuttons:
            count+= 1
            button.connect('clicked',self.add_num,count)
            
        btn_point.connect('clicked',self.add_num,'.')

        btn_plus = gtk.Button('+')
        btn_minus = gtk.Button('-')
        btn_multiply = gtk.Button('*')
        btn_divide = gtk.Button('/')
        btn_equals = gtk.Button('=')

        btn_plus.connect('clicked',self.add_operator,'+')
        btn_minus.connect('clicked',self.add_operator,'-')
        btn_multiply.connect('clicked',self.add_operator,'*')
        btn_divide.connect('clicked',self.add_operator,'/')
        btn_equals.connect('clicked',self.do_sum,True)

        self.lb_answer = gtk.Label(self.num1)

        buttonset =[btn_zero,btn_one,btn_two,btn_three,btn_four,\
                   btn_five,btn_six,btn_seven,btn_eight,btn_nine,\
                    btn_plus,btn_minus,btn_multiply,btn_divide,\
                    btn_equals,btn_cls,btn_exit,btn_point]
        
        for button in buttonset:
            button.set_border_width(0)

        btnrow1 = [btn_cls,btn_exit]
        btnrow2 = [btn_zero,btn_point,btn_equals,btn_plus]
        btnrow3 = [btn_one,btn_two,btn_three,btn_minus]
        btnrow4 = [btn_four,btn_five,btn_six,btn_multiply]
        btnrow5 = [btn_seven,btn_eight,btn_nine,btn_divide]
        btnrow6 = [self.lb_answer]

        btnrowset = [btnrow1,btnrow2,btnrow3,btnrow4,btnrow5,btnrow6]

        count = 0

        for btnrow in btnrowset:
            count += 1
            for button in btnrow:
                if count == 1:
                    hbox1.pack_start(button)
                elif count ==2:
                    hbox2.pack_start(button)
                elif count == 3:
                    hbox3.pack_start(button)
                elif count == 4:
                    hbox4.pack_start(button)
                elif count == 5:
                    hbox5.pack_start(button)
                elif count == 6:
                    hbox6.pack_start(button)
                else:
                    return

        hsep = gtk.HSeparator()
        hsep2 = gtk.HSeparator()

        hboxes = [hbox1,hbox2,hbox3,hbox4,hbox5,hsep2,hbox6,hsep]

        for box in hboxes:
            vbox.pack_end(box)

        self.add(vbox)
        self.show_all()

    def add_operator(self,widget,oper):
        self.do_sum(widget)
        self.lb_answer.set_label(str(self.num1))
        self.operator = oper
        self.num2 = self.num1
        self.num1 = '0'

    def do_sum(self,widget,cnfrm=False):
        if self.operator == '+':
            self.zeanswer = float(self.num2) + float(self.num1)
        elif self.operator == '-':
            self.zeanswer = float(self.num2) - float(self.num1)
        elif self.operator == '*':
            if self.num1 != '0':
                self.zeanswer = float(self.num2) * float(self.num1)
        elif self.operator == '/':
            if self.num1 != '0':
                self.zeanswer = float(self.num2) / float(self.num1)
        else:
            self.zeanswer = self.num1
        self.num1 = str(self.zeanswer)
        self.lb_answer.set_label(str(self.num1))
        if cnfrm:
            self.num2 = self.num1
            self.num1 = '0'
        
    def add_num(self,widget,num):
        num = str(num)
        if self.num1 == '0' and num != '.':
            self.num1 = num
        elif num == '.':
            if num not in self.num1:
                self.num1 += num
            else:
                pass
        else:
            self.num1 += num

        self.lb_answer.set_label(str(self.num1))
    
    def clrscr(self,widget):
        self.num1 = '0'
        self.num2 = '0'
        self.operator = '+'
        self.lb_answer.set_label(self.num1)

x = MainWindow()
gtk.main()

    
        

        
