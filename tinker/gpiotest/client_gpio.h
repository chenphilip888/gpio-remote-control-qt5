#pragma once

#include <QMainWindow>
#include <QLineEdit>
#include <QApplication>
#include <QPushButton>
#include <QSlider>
#include <QLabel>

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
    void send_lcd();
    void send_servo();
    void stop_test();

  private:
    QLineEdit *edt2;
    QString m_text;
    QSlider *sliderR;
    QSlider *sliderG;
    QSlider *sliderB;
    QLabel *labelR;
    QLabel *labelG;
    QLabel *labelB;
    QSlider *sliderServo;
    QLabel *labelServo;
    void   send_cmd( const char * cmd );
    int    sock;
};
