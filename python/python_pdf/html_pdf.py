from weasyprint import HTML
current_time = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
time = '<h2>' + 'Report created: ' + current_time + '</h2>'
title1 = '<h1>' +'Report blablalbla' + '</h1>'
string = title1 + time + '<p style="page-break-before: always" ></p>' # page break

#add in a table
df1 = DataFrame({'Column_A': np.arange(8), 'Column_B': list('aabbbbcc')})
string += df1.to_html(index=False)
string += '\n'
string += '<p style="page-break-before: always" ></p>'

HTML(string=string).write_pdf("report.pdf",stylesheets=["style.css"])
