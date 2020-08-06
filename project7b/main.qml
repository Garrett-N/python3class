import QtQuick 2.7
import QtQuick.Window 2.2
import QtQuick.Controls 1.4
import QtGraphicalEffects 1.0

ApplicationWindow {
    id: mainWindow
    height: 160
    width: 300
    visible: true
    title: "My Window"

    Item {
        id: page
        visible: true

        width: parent.width

        Rectangle {
            id: myrectangle
            height: {
                console.log("I\'m a comment")
                return 160
            }
            width: parent.width

            color: "#ff0000"

            Text {
                id: mainText
                text: "I am some regular text"
                height: 50
                width: parent.width
                font.pixelSize: 12
                horizontalAlignment: Text.AlignHCenter
                color: "#aaa"
            }

            Button {
                id: mainbutton
                text: "Push Me"
                anchors.top: mainText.bottom
                onClicked: {
                    if(myrectangle.color == "#ff0000"){
                        myrectangle.color = "#000"
                    }else{
                        myrectangle.color = "#f00"
                    }
                }
            }
        }
    }
}