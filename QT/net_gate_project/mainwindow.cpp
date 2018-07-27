#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui ->setupUi(this);

    this ->setFixedSize(1000, 600);
    connect(ui ->button_exit, &QPushButton::pressed, this, &QMainWindow::close);
    connect(ui ->button_stop, &QPushButton::clicked, this, &MainWindow::button_handle_stop);
    connect(ui ->button_resume, &QPushButton::clicked, this, &MainWindow::button_handle_resume);

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::button_handle_resume(void)
{
    qDebug() << "button resume";

}

void MainWindow::button_handle_stop(void)
{
    static int counter = 1;

    counter++;
    if(counter % 2 == 0){
        ui ->button_stop ->setText("RESUME");
        qDebug() << "button RESUM";
    }
    else{
        ui ->button_stop ->setText("STOP");
        qDebug() << "button stop";
    }
}
