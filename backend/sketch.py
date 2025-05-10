import cv2

def pencil_sketch(inp_img, colored):
  gray, color  = cv2.pencilSketch(inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
  if colored:
    return color
  return gray

def cartoonize(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 7)
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                   cv2.ADAPTIVE_THRESH_MEAN_C,
                                   cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def watercolor_style(image):
    return cv2.stylization(image, sigma_s=60, sigma_r=0.6)

def water_sketch(image):
    sketch = pencil_sketch(image, False)
    water_styled = watercolor_style(image)
    blend = cv2.addWeighted(sketch, 0.5, water_styled, 0.5, 0)
    return blend

def find_contours(inp_img):
   t_lower = 0
   t_upper = 1000
   aperture_size = 5
   edges = cv2.Canny(inp_img, t_lower, t_upper, apertureSize=aperture_size)
   return edges

def noodlefy(inp_img):
   t_lower = 0
   t_upper = 10
   aperture_size = 5
   edges = cv2.Canny(inp_img, t_lower, t_upper, apertureSize=aperture_size)
   return edges