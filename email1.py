import sendgrid

sg = sendgrid.SendGridClient('vickiniu', 'sendgrid01')

message = sendgrid.Mail()
message.add_to('Vicki Niu <vicki.niu@gmail.com>')
message.set_subject('Welcome to College Checklist!')
message.set_text('Hi there!\nWe hope that you\'re enjoying using College Checklist and that you will continue on with the college application process.\n'
					+'In a few weeks, you should be getting a reminder to register for the SAT: in the meantime, feel free to explore some practice materials'
					+' on the CollegeBoard website.')
message.set_from('College Checklist <info@collegechecklist.com>')
status, msg = sg.send(message)

#or
status, msg = sg.send(message)