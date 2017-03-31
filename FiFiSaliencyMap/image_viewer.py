# -*- coding:utf-8 -*-
  
import sys




from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

Signal = pyqtSignal
Slot = pyqtSlot
  

# /////////////////////////////////////////////////////////////////////////////
# ?r???[???\?????邽?߂̃V?[???B                                             //
# /////////////////////////////////////////////////////////////////////////////
class ImageViewScene( QGraphicsScene ):
    def __init__( self, *argv, **keywords ):
        super( ImageViewScene, self ).__init__( *argv, **keywords )
        self.__imageItem     = None
        self.__currentPos    = None
        self.__pressedButton = None


  
    def setFile( self, filepath ):
        # ?C???[?W???A?C?e???Ƃ??ăV?[???ɒǉ????邽?߂̃??\?b?h?B
        pixmap = QPixmap( filepath )
  
        # ???ɃV?[????Pixmap?A?C?e?????????ꍇ?͍폜?????B
        if self.__imageItem:
            self.removeItem( self.__imageItem )
  
  
        # ?^?????ꂽ?C???[?W??Pixmap?A?C?e???Ƃ??ăV?[???ɒǉ??????B-----------
        item = QGraphicsPixmapItem( pixmap )
        # ?A?C?e?????ړ??\?A?C?e???Ƃ??Đݒ??B
        item.setFlags(
            QGraphicsItem.ItemIsMovable
        )
        self.addItem( item )
        self.__imageItem = item
        # ---------------------------------------------------------------------
  
        self.fitImage()
  
    def imageItem( self ):
        return self.__imageItem

          
    def resizeEvent( self, event ):
        # ?r???[?????T?C?Y???ɃV?[???̋??`???X?V?????B
        self.fitImage()
  
    def fitImage( self ):
        # ?C???[?W???V?[???̃T?C?Y?ɍ??킹?ăt?B?b?g???邽?߂̃??\?b?h?B
        # ?A?X?y?N?g???ɂ????ďc?Ƀt?B?b?g???邩???Ƀt?B?b?g???邩???????I??
        # ???肷???B
        if not self.imageItem():
            return
  
        # ?C???[?W?̌??̑傫????????Rect?I?u?W?F?N?g?B
        boundingRect = self.imageItem().boundingRect()
        # ?V?[???̌??݂̑傫????????Rect?I?u?W?F?N?g?B
        sceneRect    = self.sceneRect()
  
        itemAspectRatio  = boundingRect.width() / boundingRect.height()
        sceneAspectRatio = sceneRect.width() / sceneRect.height()
  
        # ?ŏI?I?ɃC???[?W?̃A?C?e???ɓK?????邽?߂?Transform?I?u?W?F?N?g?B
        transform        = QTransform()
  
        if itemAspectRatio >= sceneAspectRatio:
            # ?????ɍ??킹?ăt?B?b?g?B
            scaleRatio = sceneRect.width() / boundingRect.width()
        else:
            # ?c?̍????ɍ??킹?ăt?B?b?g?B.
            scaleRatio = sceneRect.height() / boundingRect.height()
  
        # ?A?X?y?N?g?䂩???X?P?[???????????o??Transform?I?u?W?F?N?g?ɓK???B
        transform.scale( scaleRatio, scaleRatio )
        # ?ϊ????ꂽTransform?I?u?W?F?N?g???C???[?W?A?C?e???ɓK???B
        self.imageItem().setTransform( transform )
  
    def mouseDoubleClickEvent( self, event ):
        self.fitImage()
  
# /////////////////////////////////////////////////////////////////////////////
#                                                                            //
# /////////////////////////////////////////////////////////////////////////////
  
  
  
          
  
# /////////////////////////////////////////////////////////////////////////////
# ???C???ƂȂ??r???[?B                                                       //
# /////////////////////////////////////////////////////////////////////////////
class ImageViewer( QGraphicsView ):
    def __init__( self ):
        super( ImageViewer, self ).__init__( )

        self.setAcceptDrops(True)  # D&D Flag

        self.setBackgroundBrush(QBrush(Qt.darkGray));

        # QGraphicsView?̐ݒ??B------------------------------------------------
        self.setCacheMode( QGraphicsView.CacheBackground )

        self.setRenderHints( QPainter.Antialiasing |
            QPainter.SmoothPixmapTransform |
            QPainter.TextAntialiasing
        )
        # ---------------------------------------------------------------------
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        # QGraphicsScene?̍쐬?E?????ѐݒ??B------------------------------------
        scene = ImageViewScene( self )
        scene.setSceneRect( QRectF( self.rect() ) )
        self.setScene( scene )
        #scene.setFile( imagepath )
        # ---------------------------------------------------------------------
  
    def setFile( self, filepath ):
        # ?r???[?????V?[???Ƀt?@?C???p?X???n???ď???????????
        # ???s???郁?\?b?h?B
        self.scene().setFile( filepath )
          
    def resizeEvent( self, event ):
        # ?r???[?????T?C?Y???ɃV?[???̋??`???X?V?????B
        super( ImageViewer, self ).resizeEvent( event )
        self.scene().setSceneRect( QRectF( self.rect() ) )
        self.scene().fitImage()

    def dragEnterEvent(self, event):
        self.parent().dragEnterEvent(event)

    def dropEvent(self, event):
        self.parent().dropEvent(event)



# /////////////////////////////////////////////////////////////////////////////
#                                                                            //
# /////////////////////////////////////////////////////////////////////////////
  
  
if __name__ == '__main__':
    app = QApplication( sys.argv )
    viewer = ImageViewer()
    # QGraphicsScene?ɃC???[?W?p?X???Z?b?g?????B
    viewer.setFile( imagepath )
    viewer.show()
      
    sys.exit( app.exec_() )