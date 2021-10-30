#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <string>
#include <iostream>
using std::string;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    std::string str = "Hello";
    QString qs = QString::fromStdString(str);
    ui->textEdit->append(qs);
#if QT_VERSION_MAJOR < 6
    ui->textEdit->append(
        QString::fromStdString(
            std::string(
                "Qt version less than 6")));
#else
    ui->textEdit->append(
        QString::fromStdString(
            std::string(
                "Qt version greater or equal 6")));
#endif
}

MainWindow::~MainWindow()
{
    delete ui;
}
