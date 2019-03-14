#include "camvideo.h"
#include "ui_camvideo.h"

CamVideo::CamVideo(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::CamVideo)
{
    ui->setupUi(this);
}

CamVideo::~CamVideo()
{
    delete ui;
}
