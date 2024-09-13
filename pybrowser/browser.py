import argparse
import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl, QTimer

def main():
  parser = argparse.ArgumentParser(description='Simple Browser')

  parser.add_argument('-u', '--url', type=str, default="https://google.com", help='URL to open')
  parser.add_argument('-f', '--fullscreen', action='store_true', help='Open in fullscreen mode')
  parser.add_argument('-r', '--refresh', type=int, default=-1, help='Refresh interval in seconds (-1 to disable)')

  args = parser.parse_args()

  app = QApplication(sys.argv)

  browser = QWebEngineView()
  browser.load(QUrl(args.url))

  if args.fullscreen:
    browser.showFullScreen()
  else:
    browser.show()

  if args.refresh > 0:
    timer = QTimer()
    timer.timeout.connect(browser.reload)
    timer.start(args.refresh * 1000) # convert to milliseconds

  app.exec_()

if __name__ == '__main__':
  main()