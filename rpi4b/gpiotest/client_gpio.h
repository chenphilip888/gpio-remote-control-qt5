#pragma once

#include <QMainWindow>
#include <QLineEdit>
#include <QApplication>
#include <QPushButton>

class Client_gpio : public QMainWindow {
    
  Q_OBJECT

  public:
    Client_gpio(QWidget *parent = 0);

  private slots:
    void start_test();
    void ledOn();
    void ledOff();
    void OnRed();
    void OnGreen();
    void OnBlue();
    void OnYellow();
    void OnCyan();
    void OnPurple();
    void OnWhite();
    void OnBlack();
    void setText(const QString &);
    void sendText();
    void servoRight();
    void servoLeft();
    void servoMiddle();
    void servoStop();
    void stop_test();

  private:
    QLineEdit *edt2;
    void   send_cmd( const char * cmd );
    int    sock;
    QString m_text;
};
