class Bitmap():
    BITMAPFILEHEADER = dict(FileType='',FileSize='',Reserved='',PixelDataOffset='')
    BITMAPINFOHEADER = dict(ImageWidth='',ImageHeight='',Planes='',BitsPerPixel='',Compression='',ImageSize='',XpixelsPerMeter='',YpixelsPerMeter='',TotalColors='',ImportantColors='')
    COLORTABLE = dict(Red='',Green='',Blue='', Reserved='')
    PIXELDATA = array()