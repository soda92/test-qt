#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include<string>
#include<iostream>
using std::string;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    std::string str = "Hello";
    QString qs = QString::fromStdString(str);
    ui->textEdit->append(qs);
    ui->textEdit->append(qs);
}

MainWindow::~MainWindow()
{
    delete ui;
}

