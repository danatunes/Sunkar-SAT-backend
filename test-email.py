import emails


message = emails.html(subject=T('Payment Receipt No.{{ billno }}'),
                      html=T('<p>Dear {{ name }}! This is a receipt...'),
                      mail_from=('ABC', 'robot@mycompany.com'))
