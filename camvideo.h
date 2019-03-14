#ifndef CAMVIDEO_H
#define CAMVIDEO_H

#include <QMainWindow>

namespace Ui {
class CamVideo;
}

class CamVideo : public QMainWindow
{
    Q_OBJECT

public:
    explicit CamVideo(QWidget *parent = nullptr);
    ~CamVideo();

private:
    Ui::CamVideo *ui;
};

#endif // CAMVIDEO_H
