#include "client_gpio.h"
#include <QGridLayout>
#include <QLabel>
#include <QStatusBar>
#include <QLineEdit>
#include <stdio.h> 
#include <sys/socket.h> 
#include <arpa/inet.h>
#include <netinet/in.h> 
#include <netdb.h>
#include <unistd.h>
#include <time.h>
#include <string.h> 
#include <stdlib.h>

#define HOST "192.168.86.34"
#define PORT 8888

int make_socket( uint16_t port )
{
    int sock;
    struct sockaddr_in serv_addr;

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
    {
        printf("\n Socket creation error \n");
        return -1;
    }

    memset(&serv_addr, '0', sizeof(serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons( port );

    // Convert IPv4 and IPv6 addresses from text to binary form
    if(inet_pton(AF_INET, HOST, &serv_addr.sin_addr)<=0)
    {
        printf("\nInvalid address/ Address not supported \n");
        return -1;
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
    {
        printf("\nConnection Failed \n");
        return -1;
    }
    return sock;
}

Client_gpio::Client_gpio(QWidget *parent)
    : QMainWindow(parent) {

  QWidget* widget = new QWidget(this);

  QPushButton *StartTestBtn = new QPushButton("Start Test", this);
  QPushButton *StopTestBtn = new QPushButton("Stop Test", this);
  QPushButton *ledOnBtn = new QPushButton("Led On", this);
  QPushButton *ledOffBtn = new QPushButton("Led Off", this);
  QPushButton *redBtn = new QPushButton("Lcd Red", this);
  QPushButton *greenBtn = new QPushButton("Lcd Green", this);
  QPushButton *blueBtn = new QPushButton("Lcd Blue", this);
  QPushButton *yellowBtn = new QPushButton("Lcd Yellow", this);
  QPushButton *cyanBtn = new QPushButton("Lcd Cyan", this);
  QPushButton *purpleBtn = new QPushButton("Lcd Purple", this);
  QPushButton *whiteBtn = new QPushButton("Lcd White", this);
  QPushButton *blackBtn = new QPushButton("Lcd Black", this);
  QPushButton *textBtn = new QPushButton("send text", this);
  QPushButton *servoRightBtn = new QPushButton("Servo Right", this);
  QPushButton *servoLeftBtn = new QPushButton("Servo Left", this);
  QPushButton *servoMiddleBtn = new QPushButton("Servo Middle", this);
  QPushButton *servoStopBtn = new QPushButton("Servo Stop", this);
  labelR = new QLabel("R", this);
  labelR->setStyleSheet("QLabel{color:rgba(255, 0, 0, 255);}");
  labelG = new QLabel("G", this);
  labelG->setStyleSheet("QLabel{color:rgba(0, 255, 0, 255);}");
  labelB = new QLabel("B", this);
  labelB->setStyleSheet("QLabel{color:rgba(0, 0, 255, 255);}");
  sliderR = new QSlider(Qt::Horizontal, this);
  sliderR->setRange(0, 255);
  sliderG = new QSlider(Qt::Horizontal, this);
  sliderG->setRange(0, 255);
  sliderB = new QSlider(Qt::Horizontal, this);
  sliderB->setRange(0, 255);
  labelServo = new QLabel("Servo", this);
  labelServo->setStyleSheet("QLabel{color:rgba(125, 64, 255, 255);}");
  sliderServo = new QSlider(Qt::Horizontal, this);
  sliderServo->setRange(50, 100);

  QGridLayout *grid = new QGridLayout(widget);
  grid->setSpacing(10);
  grid->addWidget(StartTestBtn, 0, 0);
  grid->addWidget(StopTestBtn, 0, 3);
  grid->addWidget(ledOnBtn, 1, 0);
  grid->addWidget(ledOffBtn, 1, 1);
  grid->addWidget(redBtn, 2, 0);
  grid->addWidget(greenBtn, 2, 1);
  grid->addWidget(blueBtn, 2, 2);
  grid->addWidget(yellowBtn, 2, 3);
  grid->addWidget(cyanBtn, 3, 0);
  grid->addWidget(purpleBtn, 3, 1);
  grid->addWidget(whiteBtn, 3, 2);
  grid->addWidget(blackBtn, 3, 3);

  QLineEdit *edt2 = new QLineEdit(widget);
  grid->addWidget(edt2, 3, 0, 3, 3);
  grid->addWidget(textBtn, 4, 3);
  grid->addWidget(servoRightBtn, 5, 2);
  grid->addWidget(servoLeftBtn, 5, 0);
  grid->addWidget(servoMiddleBtn, 5, 1);
  grid->addWidget(servoStopBtn, 5, 3);
  grid->addWidget(sliderR, 5, 0, 5, 3);
  grid->addWidget(labelR, 7, 3);
  grid->addWidget(sliderG, 6, 0, 6, 3);
  grid->addWidget(labelG, 8, 3);
  grid->addWidget(sliderB, 7, 0, 7, 3);
  grid->addWidget(labelB, 10, 3);
  grid->addWidget(sliderServo, 8, 0, 8, 3);
  grid->addWidget(labelServo, 11, 3);

  widget->setLayout(grid);
  setCentralWidget(widget);
  statusBar();

  connect(StartTestBtn, &QPushButton::clicked, this, &Client_gpio::start_test);
  connect(StopTestBtn, &QPushButton::clicked, this, &Client_gpio::stop_test);
  connect(ledOnBtn, &QPushButton::clicked, this, &Client_gpio::ledOn);
  connect(ledOffBtn, &QPushButton::clicked, this, &Client_gpio::ledOff);
  connect(redBtn, &QPushButton::clicked, this, &Client_gpio::OnRed);
  connect(greenBtn, &QPushButton::clicked, this, &Client_gpio::OnGreen);
  connect(blueBtn, &QPushButton::clicked, this, &Client_gpio::OnBlue);
  connect(yellowBtn, &QPushButton::clicked, this, &Client_gpio::OnYellow);
  connect(cyanBtn, &QPushButton::clicked, this, &Client_gpio::OnCyan);
  connect(purpleBtn, &QPushButton::clicked, this, &Client_gpio::OnPurple);
  connect(whiteBtn, &QPushButton::clicked, this, &Client_gpio::OnWhite);
  connect(blackBtn, &QPushButton::clicked, this, &Client_gpio::OnBlack);
  connect(edt2, &QLineEdit::textChanged, this, &Client_gpio::setText);
  connect(textBtn, &QPushButton::clicked, this, &Client_gpio::sendText);
  connect(servoRightBtn, &QPushButton::clicked, this, &Client_gpio::servoRight);
  connect(servoLeftBtn, &QPushButton::clicked, this, &Client_gpio::servoLeft);
  connect(servoMiddleBtn, &QPushButton::clicked, this, &Client_gpio::servoMiddle);
  connect(servoStopBtn, &QPushButton::clicked, this, &Client_gpio::servoStop);
  connect(sliderR, &QSlider::valueChanged, this, &Client_gpio::send_lcd);
  connect(sliderG, &QSlider::valueChanged, this, &Client_gpio::send_lcd);
  connect(sliderB, &QSlider::valueChanged, this, &Client_gpio::send_lcd);
  connect(sliderServo, &QSlider::valueChanged, this, &Client_gpio::send_servo);

  m_text = QString();
  sock = make_socket( PORT );
}

void Client_gpio::send_lcd() {
  int valread;
  char buffer[1024] = {0};
  char lcd[10];
  sprintf(lcd, "%03d%03d%03d", sliderR->value(), sliderG->value(), sliderB->value());
  send(sock , lcd, strlen(lcd) , 0 );
  valread = read( sock, buffer, 1024 );
  buffer[valread] = '\0';
  statusBar()->showMessage(buffer);
}

void Client_gpio::send_servo() {

  int valread;
  char servo[4];
  sprintf(servo, "%d", sliderServo->value() + 300);
  char buffer[1024] = {0};
  send(sock , servo, strlen(servo) , 0 );
  valread = read( sock, buffer, 1024 );
  buffer[valread] = '\0';
  statusBar()->showMessage(buffer);
}
   
void Client_gpio::send_cmd( const char * cmd ) {

  int valread;
  char buffer[1024] = {0};
  send(sock , cmd, strlen(cmd) , 0 );
  valread = read( sock, buffer, 1024 );
  buffer[valread] = '\0';
  statusBar()->showMessage(buffer);
}

void Client_gpio::ledOn() {
  const char *cmd = "led_on";
  send_cmd( cmd );
}

void Client_gpio::ledOff() {
  const char *cmd = "led_off";
  send_cmd( cmd );
}

void Client_gpio::start_test() {
  const char *cmd = "start";
  send_cmd( cmd );
}

void Client_gpio::stop_test() {
  const char *cmd = "bye";
  send_cmd( cmd );
}

void Client_gpio::OnRed() {
  const char *cmd = "lcd_red";
  send_cmd( cmd );
}

void Client_gpio::OnGreen() {
  const char *cmd = "lcd_green";
  send_cmd( cmd );
}

void Client_gpio::OnBlue() {
  const char *cmd = "lcd_blue";
  send_cmd( cmd );
}

void Client_gpio::OnYellow() {
  const char *cmd = "lcd_yellow";
  send_cmd( cmd );
}

void Client_gpio::OnCyan() {
  const char *cmd = "lcd_cyan";
  send_cmd( cmd );
}

void Client_gpio::OnPurple() {
  const char *cmd = "lcd_purple";
  send_cmd( cmd );
}

void Client_gpio::OnWhite() {
  const char *cmd = "lcd_white";
  send_cmd( cmd );
}

void Client_gpio::OnBlack() {
  const char *cmd = "lcd_black";
  send_cmd( cmd );
}

void Client_gpio::setText(const QString &t) {
  m_text = t;
  update();
}

void Client_gpio::sendText() {
  char cmd[32];

  if (! m_text.isEmpty()) {
      QByteArray inBytes = m_text.toLocal8Bit();
      strcpy( cmd, "Hello" );
      strcat( cmd, inBytes.data() );
      send_cmd( cmd );
  }
}

void Client_gpio::servoRight() {
  const char *cmd = "servo_right";
  send_cmd( cmd );
}

void Client_gpio::servoLeft() {
  const char *cmd = "servo_left";
  send_cmd( cmd );
}

void Client_gpio::servoMiddle() {
  const char *cmd = "servo_middle";
  send_cmd( cmd );
}

void Client_gpio::servoStop() {
  const char *cmd = "servo_stop";
  send_cmd( cmd );
}

int main(int argc, char *argv[]) {

  QApplication app(argc, argv);

  Client_gpio window;

  window.resize(500, 600);
  window.setWindowTitle("gpio test");
  window.show();

  return app.exec();
}
