from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np



def TitleSlide(text='Title'):
	fig=plt.figure()
	plt.text(0,0.5,text,fontsize=15)
	plt.axis('off')
	return fig
# nothing but text

def pcc(x = np.arange(0,3,.25),output_pdf,text):
	fig=plt.figure()
	plt.text(0,0.5,text,fontsize=8)
	plt.axis('off')
	output_pdf.savefig()
	plt.close(fig)
  y = np.sin(x)
  fig = plt.figure()
  fig.suptitle('Figure super-title',fontsize=12, fontweight='bold')
  ax = fig.add_subplot(111）
  ax.set_title('Figure title',color='r', fontweight='bold')
  ax.plot(x,y,'bo-')
	output_pdf.savefig()
	plt.close(fig)

with PdfPages('report.pdf') as pdf:
	fig = TitleSlide()
	pdf.savefig(fig)
	plt.close(fig)
  pcc(x = np.arange(0,3,.25),pdf,'some introduction')
  
