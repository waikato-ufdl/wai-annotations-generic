# wai-annotations-generic
wai.annotations module to make it easier to plugin custom code into a wai.annotations pipeline.

The manual is available here:

https://ufdl.cms.waikato.ac.nz/wai-annotations-manual/

## Plugins

TODO

## Examples

### Image classification

* Source
  ```bash
  TODO
  ```
  
* ISP
  ```bash
  wai-annotations convert \
    from-images-ic \
      -i "/some/where/*.jpg" \
    generic-isp-ic \
      -c wai.annotations.generic.isp.image_classification.test.TestIC \
      -o "--output dimensions" \
    to-void-ic
  ```

* Sink
  ```bash
  TODO
  ```

### Image segmentation

* Source
  ```bash
  TODO
  ```

* ISP
  ```bash
  wai-annotations convert \
    from-images-is \
      -i "/some/where/*.jpg" \
    generic-isp-is \
      -c wai.annotations.generic.isp.image_segmentation.test.TestIS \
      -o "--output dimensions" \
    to-void-is
  ```

* Sink
  ```bash
  TODO
  ```

### Object Detection

* Source
  ```bash
  TODO
  ```

* ISP
  ```bash
  wai-annotations convert \
    from-images-od \
      -i "/some/where/*.jpg" \
    generic-isp-od \
      -c wai.annotations.generic.isp.object_detection.test.TestOD \
      -o "--output dimensions" \
    to-void-od
  ```

* Sink
  ```bash
  TODO
  ```

### Speech

* Source
  ```bash
  TODO
  ```

* ISP
  ```bash
  TODO
  ```

* Sink
  ```bash
  TODO
  ```
