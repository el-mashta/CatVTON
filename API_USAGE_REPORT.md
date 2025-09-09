### API Usage Report

-   **.**:
    -   `DensePoseChartConfidencePredictorMixin`: Used in `densepose/modeling/predictors/chart_with_confidence.py`
    -   `DensePoseChartPredictor`: Used in `densepose/modeling/predictors/chart_with_confidence.py`
    -   `DensePoseEmbeddingConfidencePredictorMixin`: Used in `densepose/modeling/predictors/cse_with_confidence.py`
    -   `DensePoseEmbeddingPredictor`: Used in `densepose/modeling/predictors/cse_with_confidence.py`
    -   `build`: Used in `densepose/data/__init__.py`
    -   `builtin`: Used in `densepose/data/datasets/__init__.py`, `densepose/data/meshes/__init__.py`, `detectron2/data/datasets/__init__.py`
    -   `cascade_rcnn`: Used in `detectron2/modeling/roi_heads/__init__.py`
    -   `catalog`: Used in `detectron2/checkpoint/__init__.py`
    -   `datasets`: Used in `densepose/data/__init__.py`, `detectron2/data/__init__.py`
    -   `detection_utils`: Used in `detectron2/data/dataset_mapper.py`
    -   `hooks`: Used in `detectron2/engine/defaults.py`
    -   `resample_fine_and_coarse_segm_to_bbox`: Used in `densepose/converters/chart_output_to_chart_result.py`
    -   `rpn`: Used in `detectron2/modeling/proposal_generator/build.py`
    -   `rrpn`: Used in `detectron2/modeling/proposal_generator/build.py`
    -   `samplers`: Used in `detectron2/data/__init__.py`
    -   `transforms`: Used in `detectron2/data/__init__.py`, `detectron2/data/dataset_mapper.py`, `detectron2/data/detection_utils.py`

-   **..**:
    -   `DatasetCatalog`: Used in `detectron2/data/datasets/coco.py`
    -   `DensePoseConfidenceModelConfig`: Used in `densepose/modeling/losses/chart_with_confidences.py`
    -   `DensePoseUVConfidenceType`: Used in `densepose/modeling/losses/chart_with_confidences.py`
    -   `MetadataCatalog`: Used in `detectron2/data/datasets/coco.py`

-   **...structures**:
    -   `DensePoseChartPredictorOutput`: Used in `densepose/modeling/predictors/chart.py`
    -   `DensePoseEmbeddingPredictorOutput`: Used in `densepose/modeling/predictors/cse.py`
    -   `decorate_predictor_output_class_with_confidences`: Used in `densepose/modeling/predictors/chart_confidence.py`

-   **..anchor_generator**:
    -   `DefaultAnchorGenerator`: Used in `detectron2/modeling/meta_arch/fcos.py`
    -   `build_anchor_generator`: Used in `detectron2/modeling/meta_arch/retinanet.py`, `detectron2/modeling/proposal_generator/rpn.py`

-   **..backbone**:
    -   `Backbone`: Used in `detectron2/modeling/meta_arch/fcos.py`, `detectron2/modeling/meta_arch/rcnn.py`, `detectron2/modeling/meta_arch/retinanet.py`, ...
    -   `build_backbone`: Used in `detectron2/modeling/meta_arch/rcnn.py`, `detectron2/modeling/meta_arch/retinanet.py`, `detectron2/modeling/meta_arch/semantic_seg.py`

-   **..backbone.resnet**:
    -   `BottleneckBlock`: Used in `detectron2/modeling/roi_heads/roi_heads.py`
    -   `ResNet`: Used in `detectron2/modeling/roi_heads/roi_heads.py`

-   **..box_regression**:
    -   `Box2BoxTransform`: Used in `detectron2/modeling/meta_arch/retinanet.py`, `detectron2/modeling/proposal_generator/rpn.py`, `detectron2/modeling/roi_heads/cascade_rcnn.py`
    -   `Box2BoxTransformLinear`: Used in `detectron2/modeling/meta_arch/fcos.py`
    -   `Box2BoxTransformRotated`: Used in `detectron2/modeling/proposal_generator/rrpn.py`, `detectron2/modeling/roi_heads/rotated_fast_rcnn.py`
    -   `_dense_box_regression_loss`: Used in `detectron2/modeling/meta_arch/fcos.py`, `detectron2/modeling/meta_arch/retinanet.py`, `detectron2/modeling/proposal_generator/rpn.py`

-   **..common.coco_schedule**:
    -   `lr_multiplier_1x`: Used in `detectron2/model_zoo/configs/COCO-Detection/fcos_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.py`, ...

-   **..common.data.coco**:
    -   `dataloader`: Used in `detectron2/model_zoo/configs/COCO-Detection/fcos_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.py`, ...

-   **..common.data.coco_keypoint**:
    -   `dataloader`: Used in `detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x.py`

-   **..common.data.coco_panoptic_separated**:
    -   `dataloader`: Used in `detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.py`

-   **..common.data.constants**:
    -   `constants`: Used in `detectron2/model_zoo/configs/Misc/mmdet_mask_rcnn_R_50_FPN_1x.py`

-   **..common.models.fcos**:
    -   `model`: Used in `detectron2/model_zoo/configs/COCO-Detection/fcos_R_50_FPN_1x.py`

-   **..common.models.keypoint_rcnn_fpn**:
    -   `model`: Used in `detectron2/model_zoo/configs/COCO-Keypoints/keypoint_rcnn_R_50_FPN_1x.py`

-   **..common.models.mask_rcnn_c4**:
    -   `model`: Used in `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.py`

-   **..common.models.mask_rcnn_fpn**:
    -   `model`: Used in `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_regnetx_4gf_dds_fpn_1x.py`, `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_regnety_4gf_dds_fpn_1x.py`, ...

-   **..common.models.panoptic_fpn**:
    -   `model`: Used in `detectron2/model_zoo/configs/COCO-PanopticSegmentation/panoptic_fpn_R_50_1x.py`

-   **..common.models.retinanet**:
    -   `model`: Used in `detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.py`

-   **..common.optim**:
    -   `SGD`: Used in `detectron2/model_zoo/configs/COCO-Detection/fcos_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.py`, ...

-   **..common.train**:
    -   `train`: Used in `detectron2/model_zoo/configs/COCO-Detection/fcos_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-Detection/retinanet_R_50_FPN_1x.py`, `detectron2/model_zoo/configs/COCO-InstanceSegmentation/mask_rcnn_R_50_C4_1x.py`, ...

-   **..confidence**:
    -   `DensePoseConfidenceModelConfig`: Used in `densepose/modeling/predictors/chart_confidence.py`
    -   `DensePoseUVConfidenceType`: Used in `densepose/modeling/predictors/chart_confidence.py`

-   **..config.config**:
    -   `CfgNode`: Used in `detectron2/tracking/base_tracker.py`, `detectron2/tracking/bbox_iou_tracker.py`, `detectron2/tracking/hungarian_tracker.py`

-   **..converters**:
    -   `HFlipConverter`: Used in `densepose/modeling/test_time_augmentation.py`

-   **..data.constants**:
    -   `constants`: Used in `detectron2/model_zoo/configs/common/models/mask_rcnn_c4.py`, `detectron2/model_zoo/configs/common/models/mask_rcnn_fpn.py`, `detectron2/model_zoo/configs/common/models/mask_rcnn_vitdet.py`, ...

-   **..data.utils**:
    -   `get_class_to_mesh_name_mapping`: Used in `densepose/vis/densepose_outputs_vertex.py`

-   **..matcher**:
    -   `Matcher`: Used in `detectron2/modeling/meta_arch/retinanet.py`, `detectron2/modeling/proposal_generator/rpn.py`, `detectron2/modeling/roi_heads/cascade_rcnn.py`, ...

-   **..poolers**:
    -   `ROIPooler`: Used in `detectron2/modeling/roi_heads/cascade_rcnn.py`, `detectron2/modeling/roi_heads/roi_heads.py`, `detectron2/modeling/roi_heads/rotated_fast_rcnn.py`

-   **..postprocessing**:
    -   `detector_postprocess`: Used in `detectron2/modeling/meta_arch/dense_detector.py`, `detectron2/modeling/meta_arch/panoptic_fpn.py`, `detectron2/modeling/meta_arch/rcnn.py`
    -   `sem_seg_postprocess`: Used in `detectron2/modeling/meta_arch/panoptic_fpn.py`, `detectron2/modeling/meta_arch/semantic_seg.py`

-   **..proposal_generator**:
    -   `build_proposal_generator`: Used in `detectron2/modeling/meta_arch/rcnn.py`

-   **..proposal_generator.proposal_utils**:
    -   `add_ground_truth_to_proposals`: Used in `detectron2/modeling/roi_heads/roi_heads.py`, `detectron2/modeling/roi_heads/rotated_fast_rcnn.py`

-   **..roi_heads**:
    -   `build_roi_heads`: Used in `detectron2/modeling/meta_arch/rcnn.py`

-   **..sampling**:
    -   `subsample_labels`: Used in `detectron2/modeling/proposal_generator/rpn.py`, `detectron2/modeling/roi_heads/roi_heads.py`

-   **..structures**:
    -   `DensePoseChartPredictorOutput`: Used in `densepose/converters/builtin.py`, `densepose/vis/densepose_outputs_iuv.py`
    -   `DensePoseChartResult`: Used in `densepose/converters/to_chart_result.py`, `densepose/vis/densepose_results.py`, `densepose/vis/densepose_results_textures.py`
    -   `DensePoseChartResultWithConfidences`: Used in `densepose/converters/to_chart_result.py`
    -   `DensePoseEmbeddingPredictorOutput`: Used in `densepose/converters/builtin.py`, `densepose/vis/densepose_outputs_vertex.py`
    -   `Instances`: Used in `detectron2/tracking/base_tracker.py`

-   **..structures.mesh**:
    -   `create_mesh`: Used in `densepose/vis/densepose_outputs_vertex.py`

-   **..utils**:
    -   `initialize_module_params`: Used in `densepose/modeling/predictors/chart.py`, `densepose/modeling/predictors/chart_confidence.py`, `densepose/modeling/predictors/cse.py`, ...
    -   `maybe_prepend_base_path`: Used in `densepose/data/datasets/chimpnsee.py`, `densepose/data/datasets/coco.py`, `densepose/data/datasets/lvis.py`, ...

-   **.anchor_generator**:
    -   `ANCHOR_GENERATOR_REGISTRY`: Used in `detectron2/modeling/__init__.py`
    -   `build_anchor_generator`: Used in `detectron2/modeling/__init__.py`

-   **.api**:
    -   `*` (wildcard import): Used in `detectron2/export/__init__.py`

-   **.aspp**:
    -   `ASPP`: Used in `detectron2/layers/__init__.py`

-   **.augmentation**:
    -   `*` (wildcard import): Used in `detectron2/data/transforms/__init__.py`
    -   `Augmentation`: Used in `detectron2/data/transforms/augmentation_impl.py`
    -   `_transform_to_aug`: Used in `detectron2/data/transforms/augmentation_impl.py`

-   **.augmentation_impl**:
    -   `*` (wildcard import): Used in `detectron2/data/transforms/__init__.py`

-   **.backbone**:
    -   `Backbone`: Used in `detectron2/modeling/backbone/__init__.py`, `detectron2/modeling/backbone/build.py`, `detectron2/modeling/backbone/fpn.py`, ...

-   **.base**:
    -   `BaseConverter`: Used in `densepose/converters/hflip.py`, `densepose/converters/to_chart_result.py`, `densepose/converters/to_mask.py`
    -   `Boxes`: Used in `densepose/vis/densepose_data_points.py`, `densepose/vis/densepose_outputs_iuv.py`, `densepose/vis/densepose_outputs_vertex.py`, ...
    -   `CompoundVisualizer`: Used in `densepose/vis/extractor.py`
    -   `Image`: Used in `densepose/vis/densepose_data_points.py`, `densepose/vis/densepose_outputs_iuv.py`, `densepose/vis/densepose_outputs_vertex.py`, ...
    -   `IntTupleBox`: Used in `densepose/converters/chart_output_to_chart_result.py`, `densepose/converters/segm_to_mask.py`
    -   `MatrixVisualizer`: Used in `densepose/vis/densepose_data_points.py`, `densepose/vis/densepose_outputs_iuv.py`, `densepose/vis/densepose_outputs_vertex.py`, ...
    -   `PointsVisualizer`: Used in `densepose/vis/densepose_data_points.py`
    -   `RectangleVisualizer`: Used in `densepose/vis/bounding_box.py`
    -   `TextVisualizer`: Used in `densepose/vis/bounding_box.py`
    -   `make_int_box`: Used in `densepose/converters/chart_output_to_chart_result.py`, `densepose/converters/segm_to_mask.py`

-   **.base_tracker**:
    -   `BaseTracker`: Used in `detectron2/tracking/bbox_iou_tracker.py`, `detectron2/tracking/hungarian_tracker.py`
    -   `TRACKER_HEADS_REGISTRY`: Used in `detectron2/tracking/bbox_iou_tracker.py`, `detectron2/tracking/iou_weighted_hungarian_bbox_iou_tracker.py`, `detectron2/tracking/vanilla_hungarian_bbox_iou_tracker.py`

-   **.batch_norm**:
    -   `CycleBatchNormList`: Used in `detectron2/layers/__init__.py`
    -   `FrozenBatchNorm2d`: Used in `detectron2/layers/__init__.py`, `detectron2/layers/blocks.py`
    -   `NaiveSyncBatchNorm`: Used in `detectron2/layers/__init__.py`
    -   `get_norm`: Used in `detectron2/layers/__init__.py`, `detectron2/layers/aspp.py`, `detectron2/layers/blocks.py`

-   **.bbox_iou_tracker**:
    -   `BBoxIOUTracker`: Used in `detectron2/tracking/__init__.py`

-   **.blocks**:
    -   `CNNBlockBase`: Used in `detectron2/layers/__init__.py`
    -   `DepthwiseSeparableConv2d`: Used in `detectron2/layers/__init__.py`, `detectron2/layers/aspp.py`

-   **.box_head**:
    -   `FastRCNNConvFCHead`: Used in `detectron2/modeling/roi_heads/__init__.py`
    -   `ROI_BOX_HEAD_REGISTRY`: Used in `detectron2/modeling/roi_heads/__init__.py`
    -   `build_box_head`: Used in `detectron2/modeling/roi_heads/__init__.py`, `detectron2/modeling/roi_heads/cascade_rcnn.py`, `detectron2/modeling/roi_heads/roi_heads.py`, ...

-   **.boxes**:
    -   `BoxMode`: Used in `detectron2/structures/__init__.py`
    -   `Boxes`: Used in `detectron2/structures/__init__.py`, `detectron2/structures/masks.py`, `detectron2/structures/rotated_boxes.py`
    -   `pairwise_ioa`: Used in `detectron2/structures/__init__.py`
    -   `pairwise_iou`: Used in `detectron2/structures/__init__.py`
    -   `pairwise_point_box_distance`: Used in `detectron2/structures/__init__.py`

-   **.build**:
    -   `BACKBONE_REGISTRY`: Used in `detectron2/modeling/backbone/__init__.py`, `detectron2/modeling/backbone/fpn.py`, `detectron2/modeling/backbone/resnet.py`
    -   `META_ARCH_REGISTRY`: Used in `detectron2/modeling/meta_arch/__init__.py`, `detectron2/modeling/meta_arch/panoptic_fpn.py`, `detectron2/modeling/meta_arch/rcnn.py`, ...
    -   `PROPOSAL_GENERATOR_REGISTRY`: Used in `detectron2/modeling/proposal_generator/__init__.py`, `detectron2/modeling/proposal_generator/rpn.py`, `detectron2/modeling/proposal_generator/rrpn.py`
    -   `build_backbone`: Used in `detectron2/modeling/backbone/__init__.py`
    -   `build_batch_data_loader`: Used in `detectron2/data/benchmark.py`
    -   `build_lr_scheduler`: Used in `detectron2/solver/__init__.py`
    -   `build_model`: Used in `detectron2/modeling/meta_arch/__init__.py`
    -   `build_optimizer`: Used in `detectron2/solver/__init__.py`
    -   `build_proposal_generator`: Used in `detectron2/modeling/proposal_generator/__init__.py`
    -   `get_default_optimizer_params`: Used in `detectron2/solver/__init__.py`

-   **.builtin_meta**:
    -   `ADE20K_SEM_SEG_CATEGORIES`: Used in `detectron2/data/datasets/builtin.py`
    -   `_get_builtin_metadata`: Used in `detectron2/data/datasets/builtin.py`
    -   `_get_coco_instances_meta`: Used in `detectron2/data/datasets/lvis.py`

-   **.c10**:
    -   `Caffe2Compatible`: Used in `detectron2/export/caffe2_modeling.py`

-   **.c2_model_loading**:
    -   `align_and_update_state_dicts`: Used in `detectron2/checkpoint/detection_checkpoint.py`

-   **.caffe2_export**:
    -   `export_caffe2_detection_model`: Used in `detectron2/export/api.py`
    -   `export_onnx_model`: Used in `detectron2/export/api.py`
    -   `run_and_save_graph`: Used in `detectron2/export/api.py`

-   **.caffe2_inference**:
    -   `ProtobufDetectionModel`: Used in `detectron2/export/api.py`

-   **.caffe2_modeling**:
    -   `META_ARCH_CAFFE2_EXPORT_TYPE_MAP`: Used in `detectron2/export/api.py`, `detectron2/export/caffe2_inference.py`
    -   `convert_batched_inputs_to_c2_format`: Used in `detectron2/export/api.py`, `detectron2/export/caffe2_inference.py`

-   **.caffe2_patch**:
    -   `ROIHeadsPatcher`: Used in `detectron2/export/caffe2_modeling.py`
    -   `patch_generalized_rcnn`: Used in `detectron2/export/caffe2_modeling.py`

-   **.cascade_rcnn**:
    -   `CascadeROIHeads`: Used in `detectron2/modeling/roi_heads/__init__.py`

-   **.catalog**:
    -   `DatasetCatalog`: Used in `detectron2/data/__init__.py`, `detectron2/data/build.py`
    -   `MeshInfo`: Used in `densepose/data/meshes/builtin.py`
    -   `Metadata`: Used in `detectron2/data/__init__.py`
    -   `MetadataCatalog`: Used in `detectron2/data/__init__.py`, `detectron2/data/build.py`, `detectron2/data/detection_utils.py`
    -   `register_meshes`: Used in `densepose/data/meshes/builtin.py`

-   **.chart**:
    -   `DensePoseChartLoss`: Used in `densepose/modeling/losses/__init__.py`, `densepose/modeling/losses/chart_with_confidences.py`
    -   `DensePoseChartPredictor`: Used in `densepose/modeling/predictors/__init__.py`
    -   `DensePoseChartPredictorOutput`: Used in `densepose/structures/__init__.py`

-   **.chart_confidence**:
    -   `DensePoseChartConfidencePredictorMixin`: Used in `densepose/modeling/predictors/__init__.py`
    -   `decorate_predictor_output_class_with_confidences`: Used in `densepose/structures/__init__.py`

-   **.chart_output_hflip**:
    -   `densepose_chart_predictor_output_hflip`: Used in `densepose/converters/__init__.py`

-   **.chart_with_confidence**:
    -   `DensePoseChartWithConfidencePredictor`: Used in `densepose/modeling/predictors/__init__.py`

-   **.chart_with_confidences**:
    -   `DensePoseChartWithConfidenceLoss`: Used in `densepose/modeling/losses/__init__.py`

-   **.chimpnsee**:
    -   `register_dataset`: Used in `densepose/data/datasets/builtin.py`

-   **.cityscapes**:
    -   `load_cityscapes_instances`: Used in `detectron2/data/datasets/builtin.py`
    -   `load_cityscapes_semantic`: Used in `detectron2/data/datasets/builtin.py`

-   **.cityscapes_evaluation**:
    -   `CityscapesInstanceEvaluator`: Used in `detectron2/evaluation/__init__.py`
    -   `CityscapesSemSegEvaluator`: Used in `detectron2/evaluation/__init__.py`

-   **.cityscapes_panoptic**:
    -   `register_all_cityscapes_panoptic`: Used in `detectron2/data/datasets/builtin.py`

-   **.coco**:
    -   `BASE_DATASETS`: Used in `densepose/data/datasets/builtin.py`
    -   `DATASETS`: Used in `densepose/data/datasets/builtin.py`
    -   `convert_to_coco_json`: Used in `detectron2/data/datasets/__init__.py`
    -   `dataloader`: Used in `detectron2/model_zoo/configs/common/data/coco_keypoint.py`, `detectron2/model_zoo/configs/common/data/coco_panoptic_separated.py`
    -   `load_coco_json`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/coco_panoptic.py`
    -   `load_sem_seg`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`, `detectron2/data/datasets/coco_panoptic.py`
    -   `register_coco_instances`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`, `detectron2/data/datasets/register_coco.py`
    -   `register_datasets`: Used in `densepose/data/datasets/builtin.py`

-   **.coco_evaluation**:
    -   `COCOEvaluator`: Used in `detectron2/evaluation/__init__.py`, `detectron2/evaluation/rotated_coco_evaluation.py`
    -   `instances_to_coco_json`: Used in `detectron2/evaluation/lvis_evaluation.py`

-   **.coco_panoptic**:
    -   `register_coco_panoptic`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`
    -   `register_coco_panoptic_separated`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`, `detectron2/data/datasets/register_coco.py`

-   **.colormap**:
    -   `random_color`: Used in `detectron2/utils/video_visualizer.py`, `detectron2/utils/visualizer.py`
    -   `random_colors`: Used in `detectron2/utils/video_visualizer.py`

-   **.combined_loader**:
    -   `CombinedDataLoader`: Used in `densepose/data/__init__.py`, `densepose/data/build.py`
    -   `Loader`: Used in `densepose/data/build.py`

-   **.common**:
    -   `AspectRatioGroupedDataset`: Used in `detectron2/data/build.py`
    -   `DatasetFromList`: Used in `detectron2/data/__init__.py`, `detectron2/data/benchmark.py`, `detectron2/data/build.py`
    -   `MapDataset`: Used in `detectron2/data/__init__.py`, `detectron2/data/benchmark.py`, `detectron2/data/build.py`
    -   `ToIterableDataset`: Used in `detectron2/data/__init__.py`, `detectron2/data/build.py`

-   **.compat**:
    -   `downgrade_config`: Used in `detectron2/config/__init__.py`, `detectron2/config/config.py`
    -   `guess_version`: Used in `detectron2/config/config.py`
    -   `upgrade_config`: Used in `detectron2/config/__init__.py`, `detectron2/config/config.py`

-   **.confidence**:
    -   `DensePoseConfidenceModelConfig`: Used in `densepose/modeling/__init__.py`
    -   `DensePoseUVConfidenceType`: Used in `densepose/modeling/__init__.py`

-   **.config**:
    -   `CfgNode`: Used in `detectron2/config/__init__.py`, `detectron2/config/compat.py`, `detectron2/config/defaults.py`
    -   `configurable`: Used in `detectron2/config/__init__.py`
    -   `get_cfg`: Used in `detectron2/config/__init__.py`
    -   `global_cfg`: Used in `detectron2/config/__init__.py`
    -   `set_global_cfg`: Used in `detectron2/config/__init__.py`

-   **.converters**:
    -   `builtin`: Used in `densepose/__init__.py`

-   **.cse**:
    -   `DensePoseCseLoss`: Used in `densepose/modeling/losses/__init__.py`
    -   `DensePoseEmbeddingPredictor`: Used in `densepose/modeling/predictors/__init__.py`
    -   `DensePoseEmbeddingPredictorOutput`: Used in `densepose/structures/__init__.py`

-   **.cse.embedder**:
    -   `Embedder`: Used in `densepose/modeling/build.py`

-   **.cse_confidence**:
    -   `DensePoseEmbeddingConfidencePredictorMixin`: Used in `densepose/modeling/predictors/__init__.py`
    -   `decorate_cse_predictor_output_class_with_confidences`: Used in `densepose/structures/__init__.py`

-   **.cse_with_confidence**:
    -   `DensePoseEmbeddingWithConfidencePredictor`: Used in `densepose/modeling/predictors/__init__.py`

-   **.cycle_pix2shape**:
    -   `PixToShapeCycleLoss`: Used in `densepose/modeling/losses/cse.py`

-   **.cycle_shape2shape**:
    -   `ShapeToShapeCycleLoss`: Used in `densepose/modeling/losses/cse.py`

-   **.data.datasets**:
    -   `builtin`: Used in `densepose/__init__.py`

-   **.data_relative**:
    -   `DensePoseDataRelative`: Used in `densepose/structures/__init__.py`

-   **.dataset_mapper**:
    -   `DatasetMapper`: Used in `densepose/data/__init__.py`, `densepose/data/build.py`, `detectron2/data/__init__.py`, ...

-   **.dataset_type**:
    -   `DatasetType`: Used in `densepose/data/datasets/chimpnsee.py`

-   **.datasets.coco**:
    -   `DENSEPOSE_CSE_KEYS_WITHOUT_MASK`: Used in `densepose/data/build.py`
    -   `DENSEPOSE_IUV_KEYS_WITHOUT_MASK`: Used in `densepose/data/build.py`

-   **.datasets.dataset_type**:
    -   `DatasetType`: Used in `densepose/data/build.py`

-   **.deeplab**:
    -   `DensePoseDeepLabHead`: Used in `densepose/modeling/roi_heads/__init__.py`

-   **.defaults**:
    -   `_C`: Used in `detectron2/config/compat.py`, `detectron2/config/config.py`

-   **.deform_conv**:
    -   `DeformConv`: Used in `detectron2/layers/__init__.py`
    -   `ModulatedDeformConv`: Used in `detectron2/layers/__init__.py`

-   **.dense_detector**:
    -   `DenseDetector`: Used in `detectron2/modeling/meta_arch/__init__.py`, `detectron2/modeling/meta_arch/fcos.py`, `detectron2/modeling/meta_arch/retinanet.py`
    -   `permute_to_N_HWA_K`: Used in `detectron2/modeling/meta_arch/retinanet.py`

-   **.densepose_base**:
    -   `DensePoseBaseSampler`: Used in `densepose/data/samplers/densepose_confidence_based.py`, `densepose/data/samplers/densepose_cse_base.py`, `densepose/data/samplers/densepose_uniform.py`

-   **.densepose_coco_evaluation**:
    -   `DensePoseCocoEval`: Used in `densepose/evaluation/evaluator.py`
    -   `DensePoseEvalMode`: Used in `densepose/evaluation/evaluator.py`

-   **.densepose_confidence_based**:
    -   `DensePoseConfidenceBasedSampler`: Used in `densepose/data/samplers/__init__.py`

-   **.densepose_cse_base**:
    -   `DensePoseCSEBaseSampler`: Used in `densepose/data/samplers/densepose_cse_confidence_based.py`, `densepose/data/samplers/densepose_cse_uniform.py`

-   **.densepose_cse_confidence_based**:
    -   `DensePoseCSEConfidenceBasedSampler`: Used in `densepose/data/samplers/__init__.py`

-   **.densepose_cse_uniform**:
    -   `DensePoseCSEUniformSampler`: Used in `densepose/data/samplers/__init__.py`

-   **.densepose_results**:
    -   `DensePoseResultsVisualizer`: Used in `densepose/vis/densepose_results_textures.py`

-   **.densepose_results_textures**:
    -   `get_texture_atlas`: Used in `densepose/vis/densepose_outputs_vertex.py`

-   **.densepose_uniform**:
    -   `DensePoseUniformSampler`: Used in `densepose/data/samplers/__init__.py`, `densepose/data/samplers/densepose_cse_uniform.py`

-   **.detection_checkpoint**:
    -   `DetectionCheckpointer`: Used in `detectron2/checkpoint/__init__.py`

-   **.detection_utils**:
    -   `check_metadata_consistency`: Used in `detectron2/data/build.py`

-   **.embed**:
    -   `EmbeddingLoss`: Used in `densepose/modeling/losses/cse.py`

-   **.embed_utils**:
    -   `CseAnnotationsAccumulator`: Used in `densepose/modeling/losses/cse.py`
    -   `PackedCseAnnotations`: Used in `densepose/modeling/losses/cycle_pix2shape.py`, `densepose/modeling/losses/embed.py`, `densepose/modeling/losses/soft_embed.py`

-   **.embedder**:
    -   `Embedder`: Used in `densepose/modeling/cse/__init__.py`

-   **.evaluation**:
    -   `DensePoseCOCOEvaluator`: Used in `densepose/__init__.py`

-   **.evaluator**:
    -   `DatasetEvaluator`: Used in `detectron2/evaluation/__init__.py`, `detectron2/evaluation/cityscapes_evaluation.py`, `detectron2/evaluation/coco_evaluation.py`, ...
    -   `DatasetEvaluators`: Used in `detectron2/evaluation/__init__.py`
    -   `DensePoseCOCOEvaluator`: Used in `densepose/evaluation/__init__.py`
    -   `inference_context`: Used in `detectron2/evaluation/__init__.py`
    -   `inference_on_dataset`: Used in `detectron2/evaluation/__init__.py`

-   **.fast_rcnn**:
    -   `FastRCNNOutputLayers`: Used in `detectron2/modeling/roi_heads/__init__.py`, `detectron2/modeling/roi_heads/cascade_rcnn.py`, `detectron2/modeling/roi_heads/roi_heads.py`, ...
    -   `fast_rcnn_inference`: Used in `detectron2/modeling/roi_heads/cascade_rcnn.py`

-   **.fcos**:
    -   `FCOS`: Used in `detectron2/modeling/meta_arch/__init__.py`

-   **.filter**:
    -   `DensePoseDataFilter`: Used in `densepose/modeling/__init__.py`, `densepose/modeling/build.py`

-   **.flatten**:
    -   `TracingAdapter`: Used in `detectron2/export/__init__.py`

-   **.fpn**:
    -   `FPN`: Used in `detectron2/modeling/backbone/__init__.py`

-   **.frame_selector**:
    -   `FrameSelector`: Used in `densepose/data/video/video_keyframe_dataset.py`
    -   `FrameTsList`: Used in `densepose/data/video/video_keyframe_dataset.py`

-   **.grouped_batch_sampler**:
    -   `GroupedBatchSampler`: Used in `detectron2/data/samplers/__init__.py`

-   **.hflip**:
    -   `HFlipConverter`: Used in `densepose/converters/__init__.py`

-   **.hooks**:
    -   `*` (wildcard import): Used in `detectron2/engine/__init__.py`

-   **.hrnet**:
    -   `build_pose_hrnet_backbone`: Used in `densepose/modeling/hrfpn.py`

-   **.hungarian_tracker**:
    -   `BaseHungarianTracker`: Used in `detectron2/tracking/__init__.py`, `detectron2/tracking/vanilla_hungarian_bbox_iou_tracker.py`

-   **.image**:
    -   `ImageResizeTransform`: Used in `densepose/data/transform/__init__.py`

-   **.image_list**:
    -   `ImageList`: Used in `detectron2/structures/__init__.py`

-   **.image_list_dataset**:
    -   `ImageListDataset`: Used in `densepose/data/__init__.py`

-   **.inference**:
    -   `densepose_inference`: Used in `densepose/modeling/__init__.py`

-   **.inference_based_loader**:
    -   `InferenceBasedLoader`: Used in `densepose/data/__init__.py`, `densepose/data/build.py`
    -   `ScoreBasedFilter`: Used in `densepose/data/__init__.py`, `densepose/data/build.py`

-   **.instances**:
    -   `Instances`: Used in `detectron2/structures/__init__.py`

-   **.instantiate**:
    -   `instantiate`: Used in `detectron2/config/__init__.py`

-   **.keypoint_head**:
    -   `build_keypoint_head`: Used in `detectron2/modeling/roi_heads/roi_heads.py`

-   **.keypoints**:
    -   `Keypoints`: Used in `detectron2/structures/__init__.py`
    -   `heatmaps_to_keypoints`: Used in `detectron2/structures/__init__.py`

-   **.launch**:
    -   `*` (wildcard import): Used in `detectron2/engine/__init__.py`

-   **.lazy**:
    -   `LazyCall`: Used in `detectron2/config/__init__.py`
    -   `LazyConfig`: Used in `detectron2/config/__init__.py`

-   **.list**:
    -   `DensePoseList`: Used in `densepose/structures/__init__.py`

-   **.losses**:
    -   `DENSEPOSE_LOSS_REGISTRY`: Used in `densepose/modeling/build.py`
    -   `ciou_loss`: Used in `detectron2/layers/__init__.py`
    -   `diou_loss`: Used in `detectron2/layers/__init__.py`

-   **.lr_scheduler**:
    -   `LRMultiplier`: Used in `detectron2/solver/build.py`
    -   `LRScheduler`: Used in `detectron2/solver/build.py`
    -   `WarmupParamScheduler`: Used in `detectron2/solver/build.py`

-   **.lvis**:
    -   `DATASETS`: Used in `densepose/data/datasets/builtin.py`
    -   `get_lvis_instances_meta`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`
    -   `load_lvis_json`: Used in `detectron2/data/datasets/__init__.py`
    -   `register_datasets`: Used in `densepose/data/datasets/builtin.py`
    -   `register_lvis_instances`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`

-   **.lvis_evaluation**:
    -   `LVISEvaluator`: Used in `detectron2/evaluation/__init__.py`

-   **.lvis_v0_5_categories**:
    -   `LVIS_CATEGORIES`: Used in `detectron2/data/datasets/lvis.py`

-   **.lvis_v1_categories**:
    -   `LVIS_CATEGORIES`: Used in `detectron2/data/datasets/lvis.py`

-   **.lvis_v1_category_image_count**:
    -   `LVIS_CATEGORY_IMAGE_COUNT`: Used in `detectron2/data/datasets/lvis.py`

-   **.mask**:
    -   `MaskLoss`: Used in `densepose/modeling/losses/mask_or_segm.py`
    -   `extract_data_for_mask_loss_from_matches`: Used in `densepose/modeling/losses/cycle_pix2shape.py`

-   **.mask_from_densepose**:
    -   `MaskFromDensePoseSampler`: Used in `densepose/data/samplers/__init__.py`

-   **.mask_head**:
    -   `build_mask_head`: Used in `detectron2/modeling/roi_heads/roi_heads.py`

-   **.mask_ops**:
    -   `paste_masks_in_image`: Used in `detectron2/layers/__init__.py`

-   **.mask_or_segm**:
    -   `MaskOrSegmentationLoss`: Used in `densepose/modeling/losses/chart.py`, `densepose/modeling/losses/cse.py`

-   **.mask_rcnn_fpn**:
    -   `model`: Used in `detectron2/model_zoo/configs/common/models/cascade_rcnn.py`, `detectron2/model_zoo/configs/common/models/keypoint_rcnn_fpn.py`, `detectron2/model_zoo/configs/common/models/mask_rcnn_vitdet.py`, ...

-   **.masks**:
    -   `BitMasks`: Used in `detectron2/structures/__init__.py`
    -   `PolygonMasks`: Used in `detectron2/structures/__init__.py`
    -   `ROIMasks`: Used in `detectron2/structures/__init__.py`
    -   `polygons_to_bitmask`: Used in `detectron2/structures/__init__.py`

-   **.mesh**:
    -   `Mesh`: Used in `densepose/structures/__init__.py`
    -   `create_mesh`: Used in `densepose/structures/__init__.py`

-   **.mesh_alignment_evaluator**:
    -   `MeshAlignmentEvaluator`: Used in `densepose/evaluation/evaluator.py`

-   **.meshes**:
    -   `builtin`: Used in `densepose/data/__init__.py`

-   **.meta_arch**:
    -   `GeneralizedRCNN`: Used in `detectron2/modeling/test_time_augmentation.py`

-   **.mmdet_wrapper**:
    -   `MMDetBackbone`: Used in `detectron2/modeling/__init__.py`
    -   `MMDetDetector`: Used in `detectron2/modeling/__init__.py`

-   **.model_zoo**:
    -   `get`: Used in `detectron2/model_zoo/__init__.py`
    -   `get_checkpoint_url`: Used in `detectron2/model_zoo/__init__.py`
    -   `get_config`: Used in `detectron2/model_zoo/__init__.py`
    -   `get_config_file`: Used in `detectron2/model_zoo/__init__.py`

-   **.modeling.hrfpn**:
    -   `build_hrfpn_backbone`: Used in `densepose/__init__.py`

-   **.modeling.roi_heads**:
    -   `DensePoseROIHeads`: Used in `densepose/__init__.py`

-   **.mvit**:
    -   `MViT`: Used in `detectron2/modeling/backbone/__init__.py`

-   **.nms**:
    -   `batched_nms`: Used in `detectron2/layers/__init__.py`
    -   `batched_nms_rotated`: Used in `detectron2/layers/__init__.py`
    -   `nms`: Used in `detectron2/layers/__init__.py`
    -   `nms_rotated`: Used in `detectron2/layers/__init__.py`

-   **.panoptic_evaluation**:
    -   `COCOPanopticEvaluator`: Used in `detectron2/evaluation/__init__.py`

-   **.panoptic_fpn**:
    -   `PanopticFPN`: Used in `detectron2/modeling/meta_arch/__init__.py`

-   **.pascal_voc**:
    -   `load_voc_instances`: Used in `detectron2/data/datasets/__init__.py`
    -   `register_pascal_voc`: Used in `detectron2/data/datasets/__init__.py`, `detectron2/data/datasets/builtin.py`

-   **.pascal_voc_evaluation**:
    -   `PascalVOCDetectionEvaluator`: Used in `detectron2/evaluation/__init__.py`

-   **.postprocessing**:
    -   `detector_postprocess`: Used in `detectron2/modeling/__init__.py`, `detectron2/modeling/test_time_augmentation.py`

-   **.prediction_to_gt**:
    -   `PredictionToGroundTruthSampler`: Used in `densepose/data/samplers/__init__.py`

-   **.predictors**:
    -   `DENSEPOSE_PREDICTOR_REGISTRY`: Used in `densepose/modeling/build.py`

-   **.proposal_utils**:
    -   `_is_tracing`: Used in `detectron2/modeling/proposal_generator/rrpn.py`
    -   `find_top_rpn_proposals`: Used in `detectron2/modeling/proposal_generator/rpn.py`

-   **.rcnn**:
    -   `GeneralizedRCNN`: Used in `detectron2/modeling/meta_arch/__init__.py`, `detectron2/modeling/meta_arch/panoptic_fpn.py`
    -   `ProposalNetwork`: Used in `detectron2/modeling/meta_arch/__init__.py`

-   **.registry**:
    -   `DENSEPOSE_LOSS_REGISTRY`: Used in `densepose/modeling/losses/__init__.py`, `densepose/modeling/losses/chart.py`, `densepose/modeling/losses/chart_with_confidences.py`, ...
    -   `DENSEPOSE_PREDICTOR_REGISTRY`: Used in `densepose/modeling/predictors/__init__.py`, `densepose/modeling/predictors/chart.py`, `densepose/modeling/predictors/chart_with_confidence.py`, ...
    -   `ROI_DENSEPOSE_HEAD_REGISTRY`: Used in `densepose/modeling/roi_heads/__init__.py`, `densepose/modeling/roi_heads/deeplab.py`, `densepose/modeling/roi_heads/v1convx.py`

-   **.regnet**:
    -   `RegNet`: Used in `detectron2/modeling/backbone/__init__.py`

-   **.resnet**:
    -   `build_resnet_backbone`: Used in `detectron2/modeling/backbone/fpn.py`

-   **.retinanet**:
    -   `RetinaNet`: Used in `detectron2/modeling/meta_arch/__init__.py`
    -   `RetinaNetHead`: Used in `detectron2/modeling/meta_arch/fcos.py`
    -   `model`: Used in `detectron2/model_zoo/configs/common/models/fcos.py`

-   **.roi_align**:
    -   `ROIAlign`: Used in `detectron2/layers/__init__.py`
    -   `roi_align`: Used in `detectron2/layers/__init__.py`

-   **.roi_align_rotated**:
    -   `ROIAlignRotated`: Used in `detectron2/layers/__init__.py`
    -   `roi_align_rotated`: Used in `detectron2/layers/__init__.py`

-   **.roi_head**:
    -   `Decoder`: Used in `densepose/modeling/roi_heads/__init__.py`
    -   `DensePoseROIHeads`: Used in `densepose/modeling/roi_heads/__init__.py`

-   **.roi_heads**:
    -   `ROI_HEADS_REGISTRY`: Used in `detectron2/modeling/roi_heads/cascade_rcnn.py`, `detectron2/modeling/roi_heads/rotated_fast_rcnn.py`
    -   `StandardROIHeads`: Used in `detectron2/modeling/roi_heads/cascade_rcnn.py`, `detectron2/modeling/roi_heads/rotated_fast_rcnn.py`

-   **.roi_heads.fast_rcnn**:
    -   `fast_rcnn_inference_single_image`: Used in `detectron2/modeling/test_time_augmentation.py`

-   **.roi_heads.registry**:
    -   `ROI_DENSEPOSE_HEAD_REGISTRY`: Used in `densepose/modeling/build.py`

-   **.rotated_boxes**:
    -   `RotatedBoxes`: Used in `detectron2/structures/__init__.py`
    -   `pairwise_iou`: Used in `detectron2/structures/__init__.py`

-   **.rotated_coco_evaluation**:
    -   `RotatedCOCOEvaluator`: Used in `detectron2/evaluation/__init__.py`

-   **.rotated_fast_rcnn**:
    -   `RROIHeads`: Used in `detectron2/modeling/roi_heads/__init__.py`

-   **.rpn**:
    -   `RPN`: Used in `detectron2/modeling/proposal_generator/__init__.py`, `detectron2/modeling/proposal_generator/rrpn.py`
    -   `RPN_HEAD_REGISTRY`: Used in `detectron2/modeling/proposal_generator/__init__.py`
    -   `StandardRPNHead`: Used in `detectron2/modeling/proposal_generator/__init__.py`
    -   `build_rpn_head`: Used in `detectron2/modeling/proposal_generator/__init__.py`

-   **.samplers**:
    -   `TrainingSampler`: Used in `detectron2/data/benchmark.py`

-   **.segm**:
    -   `SegmentationLoss`: Used in `densepose/modeling/losses/mask_or_segm.py`

-   **.sem_seg_evaluation**:
    -   `SemSegEvaluator`: Used in `detectron2/evaluation/__init__.py`

-   **.semantic_seg**:
    -   `SEM_SEG_HEADS_REGISTRY`: Used in `detectron2/modeling/meta_arch/__init__.py`
    -   `SemanticSegmentor`: Used in `detectron2/modeling/meta_arch/__init__.py`
    -   `build_sem_seg_head`: Used in `detectron2/modeling/meta_arch/__init__.py`, `detectron2/modeling/meta_arch/panoptic_fpn.py`

-   **.shape_spec**:
    -   `ShapeSpec`: Used in `detectron2/layers/__init__.py`

-   **.shared**:
    -   `ScopedWS`: Used in `detectron2/export/caffe2_inference.py`
    -   `alias`: Used in `detectron2/export/c10.py`
    -   `get_pb_arg_vali`: Used in `detectron2/export/api.py`, `detectron2/export/caffe2_inference.py`
    -   `get_pb_arg_vals`: Used in `detectron2/export/api.py`, `detectron2/export/caffe2_inference.py`
    -   `infer_device_type`: Used in `detectron2/export/caffe2_inference.py`
    -   `save_graph`: Used in `detectron2/export/api.py`
    -   `to_device`: Used in `detectron2/export/c10.py`

-   **.soft_embed**:
    -   `SoftEmbeddingLoss`: Used in `densepose/modeling/losses/cse.py`

-   **.structures**:
    -   `DensePoseDataRelative`: Used in `densepose/__init__.py`
    -   `DensePoseList`: Used in `densepose/__init__.py`
    -   `DensePoseTransformData`: Used in `densepose/__init__.py`

-   **.swin**:
    -   `SwinTransformer`: Used in `detectron2/modeling/backbone/__init__.py`

-   **.test_time_augmentation**:
    -   `DatasetMapperTTA`: Used in `detectron2/modeling/__init__.py`
    -   `GeneralizedRCNNWithTTA`: Used in `detectron2/modeling/__init__.py`

-   **.testing**:
    -   `print_csv_format`: Used in `detectron2/evaluation/__init__.py`
    -   `verify_results`: Used in `detectron2/evaluation/__init__.py`

-   **.to_chart_result**:
    -   `ToChartResultConverter`: Used in `densepose/converters/__init__.py`
    -   `ToChartResultConverterWithConfidences`: Used in `densepose/converters/__init__.py`

-   **.to_mask**:
    -   `ImageSizeType`: Used in `densepose/converters/segm_to_mask.py`
    -   `ToMaskConverter`: Used in `densepose/converters/__init__.py`

-   **.torchscript**:
    -   `dump_torchscript_IR`: Used in `detectron2/export/__init__.py`
    -   `scripting_with_instances`: Used in `detectron2/export/__init__.py`

-   **.torchscript_patch**:
    -   `freeze_training_mode`: Used in `detectron2/export/torchscript.py`
    -   `patch_builtin_len`: Used in `detectron2/export/flatten.py`
    -   `patch_instances`: Used in `detectron2/export/torchscript.py`

-   **.train_loop**:
    -   `*` (wildcard import): Used in `detectron2/engine/__init__.py`
    -   `AMPTrainer`: Used in `detectron2/engine/defaults.py`
    -   `HookBase`: Used in `detectron2/engine/hooks.py`
    -   `SimpleTrainer`: Used in `detectron2/engine/defaults.py`
    -   `TrainerBase`: Used in `detectron2/engine/defaults.py`

-   **.trainer**:
    -   `Trainer`: Used in `densepose/engine/__init__.py`

-   **.transform**:
    -   `*` (wildcard import): Used in `detectron2/data/transforms/__init__.py`
    -   `ExtentTransform`: Used in `detectron2/data/transforms/augmentation_impl.py`
    -   `ImageResizeTransform`: Used in `densepose/data/build.py`
    -   `ResizeTransform`: Used in `detectron2/data/transforms/augmentation_impl.py`
    -   `RotationTransform`: Used in `detectron2/data/transforms/augmentation_impl.py`

-   **.transform_data**:
    -   `DensePoseTransformData`: Used in `densepose/structures/__init__.py`
    -   `normalized_coords_transform`: Used in `densepose/structures/__init__.py`

-   **.utils**:
    -   `AnnotationsAccumulator`: Used in `densepose/modeling/losses/embed_utils.py`
    -   `BilinearInterpolationHelper`: Used in `densepose/modeling/losses/chart_with_confidences.py`, `densepose/modeling/losses/cse.py`, `densepose/modeling/losses/embed.py`, ...
    -   `LossDict`: Used in `densepose/modeling/losses/chart_with_confidences.py`, `densepose/modeling/losses/cse.py`
    -   `create_prediction_pairs`: Used in `detectron2/tracking/__init__.py`
    -   `extract_packed_annotations_from_matches`: Used in `densepose/modeling/losses/cse.py`
    -   `get_category_to_class_mapping`: Used in `densepose/data/build.py`
    -   `get_class_to_mesh_name_mapping`: Used in `densepose/data/build.py`
    -   `initialize_module_params`: Used in `densepose/modeling/__init__.py`
    -   `is_relative_local_path`: Used in `densepose/data/__init__.py`
    -   `maybe_prepend_base_path`: Used in `densepose/data/__init__.py`
    -   `normalize_embeddings`: Used in `densepose/modeling/cse/vertex_direct_embedder.py`, `densepose/modeling/cse/vertex_feature_embedder.py`
    -   `resample_data`: Used in `densepose/modeling/losses/segm.py`
    -   `sample_random_indices`: Used in `densepose/modeling/losses/cycle_shape2shape.py`

-   **.utils.env**:
    -   `setup_environment`: Used in `detectron2/__init__.py`

-   **.utils.transform**:
    -   `load_from_cfg`: Used in `densepose/__init__.py`

-   **.v1convx**:
    -   `DensePoseV1ConvXHead`: Used in `densepose/modeling/roi_heads/__init__.py`

-   **.vanilla_hungarian_bbox_iou_tracker**:
    -   `VanillaHungarianBBoxIOUTracker`: Used in `detectron2/tracking/__init__.py`, `detectron2/tracking/iou_weighted_hungarian_bbox_iou_tracker.py`

-   **.vertex_direct_embedder**:
    -   `VertexDirectEmbedder`: Used in `densepose/modeling/cse/__init__.py`, `densepose/modeling/cse/embedder.py`

-   **.vertex_feature_embedder**:
    -   `VertexFeatureEmbedder`: Used in `densepose/modeling/cse/__init__.py`, `densepose/modeling/cse/embedder.py`

-   **.vit**:
    -   `SimpleFeaturePyramid`: Used in `detectron2/modeling/backbone/__init__.py`
    -   `ViT`: Used in `detectron2/modeling/backbone/__init__.py`
    -   `get_vit_lr_decay_rate`: Used in `detectron2/modeling/backbone/__init__.py`

-   **.wrappers**:
    -   `BatchNorm2d`: Used in `detectron2/layers/batch_norm.py`
    -   `Conv2d`: Used in `detectron2/layers/aspp.py`, `detectron2/layers/blocks.py`
    -   `_NewEmptyTensorOp`: Used in `detectron2/layers/deform_conv.py`

-   **PIL**:
    -   `PIL` (module import): Used in `detectron2/utils/collect_env.py`, `model/pipeline.py`, `utils.py`
    -   `Image`: Used in `app.py`, `app_flux.py`, `app_p2p.py`, ...
    -   `ImageFilter`: Used in `inference.py`

-   **__future__**:
    -   `absolute_import`: Used in `densepose/modeling/hrnet.py`, `detectron2/layers/rotated_boxes.py`, `model/SCHP/networks/__init__.py`, ...
    -   `division`: Used in `densepose/modeling/hrnet.py`, `detectron2/layers/rotated_boxes.py`, `detectron2/structures/image_list.py`, ...
    -   `print_function`: Used in `densepose/modeling/hrnet.py`, `detectron2/layers/rotated_boxes.py`, `model/SCHP/utils/transforms.py`
    -   `unicode_literals`: Used in `detectron2/layers/rotated_boxes.py`

-   **accelerate**:
    -   `accelerate` (module import): Used in `utils.py`
    -   `Accelerator`: Used in `utils.py`
    -   `DistributedDataParallelKwargs`: Used in `utils.py`
    -   `load_checkpoint_in_model`: Used in `model/pipeline.py`

-   **accelerate.state**:
    -   `AcceleratorState`: Used in `utils.py`

-   **accelerate.utils**:
    -   `ProjectConfiguration`: Used in `utils.py`

-   **ast**:
    -   `ast` (module import): Used in `detectron2/config/lazy.py`

-   **atexit**:
    -   `atexit` (module import): Used in `detectron2/utils/logger.py`

-   **av**:
    -   `av` (module import): Used in `densepose/data/video/video_keyframe_dataset.py`

-   **base64**:
    -   `base64` (module import): Used in `densepose/structures/chart_result.py`

-   **bisect**:
    -   `bisect_right`: Used in `detectron2/solver/lr_scheduler.py`

-   **black**:
    -   `black` (module import): Used in `detectron2/config/lazy.py`

-   **builtins**:
    -   `builtins` (module import): Used in `densepose/utils/dbhelper.py`, `detectron2/config/lazy.py`

-   **caffe2.proto**:
    -   `caffe2_pb2`: Used in `detectron2/export/__init__.py`, `detectron2/export/api.py`, `detectron2/export/caffe2_export.py`, ...

-   **caffe2.python**:
    -   `core`: Used in `detectron2/export/__init__.py`, `detectron2/export/caffe2_export.py`, `detectron2/export/caffe2_inference.py`, ...
    -   `net_drawer`: Used in `detectron2/export/shared.py`
    -   `workspace`: Used in `detectron2/export/shared.py`

-   **caffe2.python.onnx.backend**:
    -   `Caffe2Backend`: Used in `detectron2/export/caffe2_export.py`

-   **caffe2.python.utils**:
    -   `caffe2.python.utils` (module import): Used in `detectron2/export/shared.py`

-   **cityscapesscripts.evaluation.evalInstanceLevelSemanticLabeling**:
    -   `cityscapesscripts.evaluation.evalInstanceLevelSemanticLabeling` (module import): Used in `detectron2/evaluation/cityscapes_evaluation.py`

-   **cityscapesscripts.evaluation.evalPixelLevelSemanticLabeling**:
    -   `cityscapesscripts.evaluation.evalPixelLevelSemanticLabeling` (module import): Used in `detectron2/evaluation/cityscapes_evaluation.py`

-   **cityscapesscripts.helpers.labels**:
    -   `id2label`: Used in `detectron2/data/datasets/cityscapes.py`
    -   `labels`: Used in `detectron2/data/datasets/cityscapes.py`
    -   `name2label`: Used in `detectron2/data/datasets/cityscapes.py`, `detectron2/evaluation/cityscapes_evaluation.py`
    -   `trainId2label`: Used in `detectron2/evaluation/cityscapes_evaluation.py`

-   **cleanfid**:
    -   `fid`: Used in `eval.py`

-   **cloudpickle**:
    -   `cloudpickle` (module import): Used in `detectron2/config/lazy.py`, `detectron2/utils/serialize.py`

-   **colorsys**:
    -   `colorsys` (module import): Used in `detectron2/utils/visualizer.py`

-   **concurrent.futures**:
    -   `concurrent.futures` (module import): Used in `detectron2/engine/train_loop.py`

-   **contextlib**:
    -   `contextlib` (module import): Used in `densepose/data/datasets/coco.py`, `densepose/evaluation/evaluator.py`, `detectron2/data/common.py`, ...
    -   `ExitStack`: Used in `detectron2/evaluation/evaluator.py`, `detectron2/export/torchscript_patch.py`
    -   `asynccontextmanager`: Used in `app_sd_volume.py`
    -   `contextmanager`: Used in `detectron2/config/lazy.py`, `detectron2/evaluation/evaluator.py`, `detectron2/export/torchscript_patch.py`, ...

-   **csv**:
    -   `csv` (module import): Used in `densepose/data/video/video_keyframe_dataset.py`

-   **dataclasses**:
    -   `dataclasses` (module import): Used in `detectron2/config/instantiate.py`
    -   `dataclass`: Used in `densepose/data/build.py`, `densepose/data/datasets/coco.py`, `densepose/data/meshes/catalog.py`, ...
    -   `fields`: Used in `densepose/converters/chart_output_hflip.py`, `densepose/modeling/inference.py`
    -   `is_dataclass`: Used in `detectron2/config/lazy.py`
    -   `make_dataclass`: Used in `densepose/structures/chart_confidence.py`, `densepose/structures/cse_confidence.py`

-   **datetime**:
    -   `datetime` (module import): Used in `densepose/evaluation/densepose_coco_evaluation.py`, `detectron2/data/datasets/coco.py`, `detectron2/engine/hooks.py`, ...
    -   `datetime`: Used in `app.py`, `app_flux.py`, `app_p2p.py`, ...
    -   `timedelta`: Used in `detectron2/engine/launch.py`

-   **diffusers**:
    -   `AutoencoderKL`: Used in `model/pipeline.py`, `model/utils.py`
    -   `DDIMScheduler`: Used in `model/pipeline.py`
    -   `SchedulerMixin`: Used in `utils.py`
    -   `UNet2DConditionModel`: Used in `model/pipeline.py`, `utils.py`

-   **diffusers.configuration_utils**:
    -   `ConfigMixin`: Used in `model/flux/transformer_flux.py`
    -   `register_to_config`: Used in `model/flux/transformer_flux.py`

-   **diffusers.image_processor**:
    -   `VaeImageProcessor`: Used in `app.py`, `app_flux.py`, `app_p2p.py`, ...

-   **diffusers.loaders**:
    -   `FromOriginalModelMixin`: Used in `model/flux/transformer_flux.py`
    -   `PeftAdapterMixin`: Used in `model/flux/transformer_flux.py`

-   **diffusers.models.attention**:
    -   `FeedForward`: Used in `model/flux/transformer_flux.py`

-   **diffusers.models.autoencoders**:
    -   `AutoencoderKL`: Used in `model/flux/pipeline_flux_tryon.py`

-   **diffusers.models.embeddings**:
    -   `CombinedTimestepGuidanceTextProjEmbeddings`: Used in `model/flux/transformer_flux.py`
    -   `CombinedTimestepTextProjEmbeddings`: Used in `model/flux/transformer_flux.py`
    -   `FluxPosEmbed`: Used in `model/flux/transformer_flux.py`
    -   `apply_rotary_emb`: Used in `model/flux/transformer_flux.py`

-   **diffusers.models.modeling_outputs**:
    -   `Transformer2DModelOutput`: Used in `model/flux/transformer_flux.py`

-   **diffusers.models.modeling_utils**:
    -   `ModelMixin`: Used in `model/flux/transformer_flux.py`

-   **diffusers.models.normalization**:
    -   `AdaLayerNormContinuous`: Used in `model/flux/transformer_flux.py`
    -   `AdaLayerNormZero`: Used in `model/flux/transformer_flux.py`
    -   `AdaLayerNormZeroSingle`: Used in `model/flux/transformer_flux.py`

-   **diffusers.pipelines.flux.pipeline_output**:
    -   `FluxPipelineOutput`: Used in `model/flux/pipeline_flux_tryon.py`

-   **diffusers.pipelines.pipeline_utils**:
    -   `DiffusionPipeline`: Used in `model/flux/pipeline_flux_tryon.py`

-   **diffusers.schedulers**:
    -   `FlowMatchEulerDiscreteScheduler`: Used in `model/flux/pipeline_flux_tryon.py`

-   **diffusers.utils**:
    -   `USE_PEFT_BACKEND`: Used in `model/flux/transformer_flux.py`
    -   `is_torch_version`: Used in `model/flux/transformer_flux.py`
    -   `logging`: Used in `model/flux/pipeline_flux_tryon.py`, `model/flux/transformer_flux.py`
    -   `scale_lora_layers`: Used in `model/flux/transformer_flux.py`
    -   `unscale_lora_layers`: Used in `model/flux/transformer_flux.py`

-   **diffusers.utils.torch_utils**:
    -   `maybe_allow_in_graph`: Used in `model/flux/transformer_flux.py`
    -   `randn_tensor`: Used in `model/flux/pipeline_flux_tryon.py`, `model/pipeline.py`

-   **enum**:
    -   `Enum`: Used in `densepose/data/datasets/dataset_type.py`, `densepose/data/video/frame_selector.py`, `densepose/evaluation/densepose_coco_evaluation.py`, ...
    -   `IntEnum`: Used in `detectron2/structures/boxes.py`
    -   `unique`: Used in `detectron2/structures/boxes.py`, `detectron2/utils/visualizer.py`

-   **fairscale.nn.checkpoint**:
    -   `checkpoint_wrapper`: Used in `detectron2/modeling/backbone/mvit.py`, `detectron2/modeling/backbone/vit.py`

-   **fastapi**:
    -   `FastAPI`: Used in `app_sd_volume.py`
    -   `HTTPException`: Used in `app_sd_volume.py`

-   **fvcore**:
    -   `fvcore` (module import): Used in `detectron2/utils/analysis.py`, `detectron2/utils/collect_env.py`, `detectron2/utils/env.py`

-   **fvcore.common.checkpoint**:
    -   `Checkpointer`: Used in `detectron2/checkpoint/__init__.py`, `detectron2/checkpoint/detection_checkpoint.py`, `detectron2/engine/hooks.py`
    -   `PeriodicCheckpointer`: Used in `detectron2/checkpoint/__init__.py`, `detectron2/engine/hooks.py`

-   **fvcore.common.config**:
    -   `CfgNode`: Used in `detectron2/config/config.py`

-   **fvcore.common.history_buffer**:
    -   `HistoryBuffer`: Used in `detectron2/utils/events.py`

-   **fvcore.common.param_scheduler**:
    -   `MultiStepParamScheduler`: Used in `detectron2/model_zoo/configs/Misc/torchvision_imagenet_R_50.py`, `detectron2/model_zoo/configs/common/coco_schedule.py`, `detectron2/model_zoo/configs/new_baselines/mask_rcnn_R_50_FPN_100ep_LSJ.py`
    -   `ParamScheduler`: Used in `detectron2/engine/hooks.py`

-   **fvcore.common.registry**:
    -   `Registry`: Used in `detectron2/utils/registry.py`

-   **fvcore.common.timer**:
    -   `Timer`: Used in `densepose/data/datasets/coco.py`, `densepose/data/datasets/lvis.py`, `detectron2/data/benchmark.py`, ...

-   **fvcore.nn**:
    -   `activation_count`: Used in `detectron2/utils/analysis.py`
    -   `flop_count`: Used in `detectron2/utils/analysis.py`
    -   `giou_loss`: Used in `detectron2/modeling/box_regression.py`
    -   `parameter_count`: Used in `detectron2/utils/analysis.py`
    -   `parameter_count_table`: Used in `detectron2/utils/analysis.py`
    -   `sigmoid_focal_loss_jit`: Used in `detectron2/modeling/meta_arch/fcos.py`, `detectron2/modeling/meta_arch/retinanet.py`
    -   `smooth_l1_loss`: Used in `detectron2/modeling/box_regression.py`

-   **fvcore.nn.distributed**:
    -   `differentiable_all_reduce`: Used in `detectron2/layers/batch_norm.py`

-   **fvcore.nn.precise_bn**:
    -   `get_bn_modules`: Used in `detectron2/engine/defaults.py`, `detectron2/engine/hooks.py`
    -   `update_bn_stats`: Used in `detectron2/engine/hooks.py`

-   **fvcore.nn.weight_init**:
    -   `fvcore.nn.weight_init` (module import): Used in `densepose/modeling/roi_heads/deeplab.py`, `densepose/modeling/roi_heads/roi_head.py`, `detectron2/layers/aspp.py`, ...

-   **fvcore.transforms**:
    -   `HFlipTransform`: Used in `densepose/modeling/test_time_augmentation.py`, `detectron2/modeling/test_time_augmentation.py`
    -   `NoOpTransform`: Used in `detectron2/modeling/test_time_augmentation.py`
    -   `TransformList`: Used in `densepose/modeling/test_time_augmentation.py`

-   **fvcore.transforms.transform**:
    -   `*` (wildcard import): Used in `detectron2/data/transforms/__init__.py`
    -   `Transform`: Used in `detectron2/data/transforms/__init__.py`, `detectron2/data/transforms/augmentation.py`
    -   `TransformList`: Used in `detectron2/data/transforms/__init__.py`, `detectron2/data/transforms/augmentation.py`

-   **gradio**:
    -   `gradio` (module import): Used in `app.py`, `app_flux.py`, `app_p2p.py`

-   **huggingface_hub**:
    -   `snapshot_download`: Used in `app.py`, `app_flux.py`, `app_p2p.py`, ...

-   **hydra.core.override_parser.overrides_parser**:
    -   `OverridesParser`: Used in `detectron2/config/lazy.py`

-   **hydra.utils**:
    -   `_locate`: Used in `detectron2/utils/registry.py`

-   **importlib**:
    -   `importlib` (module import): Used in `detectron2/config/lazy.py`, `detectron2/utils/collect_env.py`, `detectron2/utils/env.py`

-   **importlib.util**:
    -   `importlib.util` (module import): Used in `detectron2/utils/env.py`

-   **io**:
    -   `io` (module import): Used in `densepose/data/datasets/coco.py`, `densepose/evaluation/evaluator.py`, `densepose/evaluation/tensor_storage.py`, ...
    -   `BytesIO`: Used in `densepose/structures/chart_result.py`

-   **iopath**:
    -   `iopath` (module import): Used in `detectron2/utils/collect_env.py`

-   **iopath.common.file_io**:
    -   `HTTPURLHandler`: Used in `detectron2/utils/file_io.py`
    -   `OneDrivePathHandler`: Used in `detectron2/utils/file_io.py`
    -   `PathHandler`: Used in `detectron2/utils/file_io.py`
    -   `PathManager`: Used in `detectron2/utils/file_io.py`
    -   `file_lock`: Used in `detectron2/data/datasets/coco.py`

-   **lvis**:
    -   `LVIS`: Used in `densepose/data/datasets/lvis.py`, `detectron2/data/datasets/lvis.py`, `detectron2/evaluation/lvis_evaluation.py`
    -   `LVISEval`: Used in `detectron2/evaluation/lvis_evaluation.py`
    -   `LVISResults`: Used in `detectron2/evaluation/lvis_evaluation.py`

-   **matplotlib**:
    -   `matplotlib` (module import): Used in `densepose/vis/densepose_results.py`, `detectron2/utils/visualizer.py`

-   **matplotlib.backends.backend_agg**:
    -   `FigureCanvasAgg`: Used in `densepose/vis/densepose_results.py`, `detectron2/utils/visualizer.py`

-   **matplotlib.colors**:
    -   `matplotlib.colors` (module import): Used in `detectron2/utils/visualizer.py`

-   **matplotlib.figure**:
    -   `matplotlib.figure` (module import): Used in `detectron2/utils/visualizer.py`

-   **matplotlib.pyplot**:
    -   `matplotlib.pyplot` (module import): Used in `densepose/vis/densepose_results.py`

-   **mmcv.utils**:
    -   `ConfigDict`: Used in `detectron2/modeling/mmdet_wrapper.py`

-   **mmdet.core**:
    -   `BitmapMasks`: Used in `detectron2/modeling/mmdet_wrapper.py`
    -   `PolygonMasks`: Used in `detectron2/modeling/mmdet_wrapper.py`

-   **mmdet.models**:
    -   `build_backbone`: Used in `detectron2/modeling/mmdet_wrapper.py`
    -   `build_detector`: Used in `detectron2/modeling/mmdet_wrapper.py`
    -   `build_neck`: Used in `detectron2/modeling/mmdet_wrapper.py`

-   **multiprocessing**:
    -   `multiprocessing` (module import): Used in `detectron2/data/datasets/cityscapes.py`

-   **numpy**:
    -   `numpy` (module import): Used in `app.py`, `app_flux.py`, `app_p2p.py`, ...
    -   `random`: Used in `detectron2/data/transforms/augmentation_impl.py`

-   **omegaconf**:
    -   `DictConfig`: Used in `detectron2/config/config.py`, `detectron2/config/instantiate.py`, `detectron2/config/lazy.py`, ...
    -   `ListConfig`: Used in `detectron2/config/instantiate.py`, `detectron2/config/lazy.py`
    -   `OmegaConf`: Used in `detectron2/config/instantiate.py`, `detectron2/config/lazy.py`, `detectron2/engine/defaults.py`, ...
    -   `SCMode`: Used in `detectron2/config/lazy.py`

-   **onnx**:
    -   `onnx` (module import): Used in `detectron2/export/caffe2_export.py`

-   **onnx.optimizer**:
    -   `onnx.optimizer` (module import): Used in `detectron2/export/caffe2_export.py`

-   **operator**:
    -   `operator` (module import): Used in `detectron2/data/build.py`, `detectron2/engine/hooks.py`
    -   `mul`: Used in `densepose/evaluation/tensor_storage.py`

-   **packaging**:
    -   `version`: Used in `detectron2/utils/testing.py`, `utils.py`

-   **panopticapi.evaluation**:
    -   `pq_compute`: Used in `detectron2/evaluation/panoptic_evaluation.py`

-   **panopticapi.utils**:
    -   `id2rgb`: Used in `detectron2/evaluation/panoptic_evaluation.py`
    -   `rgb2id`: Used in `detectron2/utils/visualizer.py`

-   **pkg_resources**:
    -   `pkg_resources` (module import): Used in `detectron2/model_zoo/model_zoo.py`

-   **pprint**:
    -   `pprint` (module import): Used in `detectron2/data/transforms/augmentation.py`, `detectron2/evaluation/testing.py`

-   **prettytable**:
    -   `PrettyTable`: Used in `eval.py`

-   **pycocotools**:
    -   `mask`: Used in `densepose/evaluation/densepose_coco_evaluation.py`

-   **pycocotools.coco**:
    -   `COCO`: Used in `densepose/data/datasets/coco.py`, `densepose/evaluation/evaluator.py`, `detectron2/data/datasets/coco.py`, ...

-   **pycocotools.cocoeval**:
    -   `COCOeval`: Used in `detectron2/evaluation/coco_evaluation.py`, `detectron2/evaluation/fast_eval_api.py`, `detectron2/evaluation/rotated_coco_evaluation.py`
    -   `maskUtils`: Used in `detectron2/evaluation/rotated_coco_evaluation.py`

-   **pycocotools.mask**:
    -   `pycocotools.mask` (module import): Used in `densepose/evaluation/evaluator.py`, `densepose/structures/data_relative.py`, `detectron2/data/datasets/cityscapes.py`, ...

-   **pydantic**:
    -   `BaseModel`: Used in `app_sd_volume.py`

-   **pydoc**:
    -   `pydoc` (module import): Used in `detectron2/utils/registry.py`

-   **pygments**:
    -   `pygments` (module import): Used in `detectron2/engine/defaults.py`

-   **pygments.formatters**:
    -   `Terminal256Formatter`: Used in `detectron2/engine/defaults.py`

-   **pygments.lexers**:
    -   `Python3Lexer`: Used in `detectron2/engine/defaults.py`
    -   `YamlLexer`: Used in `detectron2/engine/defaults.py`

-   **scipy.io**:
    -   `scipy.io` (module import): Used in `densepose/structures/transform_data.py`
    -   `loadmat`: Used in `densepose/evaluation/densepose_coco_evaluation.py`

-   **scipy.ndimage**:
    -   `zoom`: Used in `densepose/evaluation/densepose_coco_evaluation.py`

-   **scipy.optimize**:
    -   `linear_sum_assignment`: Used in `detectron2/tracking/hungarian_tracker.py`

-   **scipy.spatial.distance**:
    -   `scipy.spatial.distance` (module import): Used in `densepose/evaluation/densepose_coco_evaluation.py`

-   **shapely.geometry**:
    -   `MultiPolygon`: Used in `detectron2/data/datasets/cityscapes.py`
    -   `Polygon`: Used in `detectron2/data/datasets/cityscapes.py`

-   **socket**:
    -   `socket` (module import): Used in `detectron2/engine/launch.py`

-   **struct**:
    -   `struct` (module import): Used in `detectron2/export/caffe2_modeling.py`

-   **tabulate**:
    -   `tabulate`: Used in `densepose/evaluation/evaluator.py`, `detectron2/data/build.py`, `detectron2/evaluation/coco_evaluation.py`, ...

-   **termcolor**:
    -   `colored`: Used in `detectron2/data/build.py`, `detectron2/export/caffe2_export.py`, `detectron2/utils/logger.py`

-   **timm.models.layers**:
    -   `DropPath`: Used in `detectron2/modeling/backbone/mvit.py`, `detectron2/modeling/backbone/swin.py`, `detectron2/modeling/backbone/vit.py`
    -   `Mlp`: Used in `detectron2/modeling/backbone/mvit.py`, `detectron2/modeling/backbone/vit.py`

-   **torch**:
    -   `torch` (module import): Used in `app.py`, `app_flux.py`, `app_p2p.py`, ...
    -   `Tensor`: Used in `detectron2/export/torchscript_patch.py`, `detectron2/modeling/meta_arch/dense_detector.py`, `detectron2/modeling/meta_arch/retinanet.py`, ...
    -   `device`: Used in `detectron2/structures/boxes.py`, `detectron2/structures/image_list.py`, `detectron2/structures/masks.py`
    -   `nn`: Used in `densepose/data/inference_based_loader.py`, `densepose/engine/trainer.py`, `densepose/evaluation/mesh_alignment_evaluator.py`, ...

-   **torch._C**:
    -   `ListType`: Used in `detectron2/utils/testing.py`

-   **torch.__config__**:
    -   `torch.__config__` (module import): Used in `detectron2/utils/collect_env.py`

-   **torch._dynamo**:
    -   `is_compiling`: Used in `detectron2/layers/wrappers.py`

-   **torch.autograd**:
    -   `Function`: Used in `detectron2/layers/deform_conv.py`, `detectron2/layers/roi_align_rotated.py`

-   **torch.autograd.function**:
    -   `Function`: Used in `detectron2/modeling/roi_heads/cascade_rcnn.py`
    -   `once_differentiable`: Used in `detectron2/layers/deform_conv.py`, `detectron2/layers/roi_align_rotated.py`

-   **torch.cuda.amp**:
    -   `GradScaler`: Used in `detectron2/engine/train_loop.py`
    -   `autocast`: Used in `detectron2/engine/train_loop.py`

-   **torch.distributed**:
    -   `torch.distributed` (module import): Used in `detectron2/engine/launch.py`, `detectron2/layers/batch_norm.py`, `detectron2/utils/collect_env.py`, ...

-   **torch.distributed.algorithms.ddp_comm_hooks**:
    -   `default`: Used in `detectron2/engine/defaults.py`

-   **torch.fx._symbolic_trace**:
    -   `_orig_module_call`: Used in `detectron2/utils/tracing.py`
    -   `is_fx_tracing`: Used in `detectron2/utils/tracing.py`

-   **torch.jit._recursive**:
    -   `concrete_type_store`: Used in `detectron2/export/torchscript_patch.py`

-   **torch.jit._state**:
    -   `_jit_caching_layer`: Used in `detectron2/export/torchscript_patch.py`

-   **torch.multiprocessing**:
    -   `torch.multiprocessing` (module import): Used in `detectron2/engine/launch.py`, `detectron2/utils/collect_env.py`

-   **torch.nn**:
    -   `torch.nn` (module import): Used in `densepose/modeling/hrfpn.py`, `densepose/modeling/hrnet.py`, `densepose/modeling/roi_heads/roi_head.py`, ...
    -   `BatchNorm2d`: Used in `model/SCHP/networks/AugmentCE2P.py`
    -   `LeakyReLU`: Used in `model/SCHP/networks/AugmentCE2P.py`
    -   `functional`: Used in `densepose/converters/chart_output_to_chart_result.py`, `densepose/converters/segm_to_mask.py`, `densepose/data/samplers/densepose_base.py`, ...

-   **torch.nn.functional**:
    -   `torch.nn.functional` (module import): Used in `densepose/evaluation/densepose_coco_evaluation.py`, `densepose/modeling/hrfpn.py`, `detectron2/data/transforms/transform.py`, ...
    -   `interpolate`: Used in `detectron2/export/shared.py`

-   **torch.nn.modules.utils**:
    -   `_pair`: Used in `detectron2/layers/deform_conv.py`, `detectron2/layers/roi_align_rotated.py`

-   **torch.nn.parallel**:
    -   `DataParallel`: Used in `detectron2/engine/train_loop.py`
    -   `DistributedDataParallel`: Used in `detectron2/checkpoint/detection_checkpoint.py`, `detectron2/engine/defaults.py`, `detectron2/engine/train_loop.py`, ...

-   **torch.onnx**:
    -   `OperatorExportTypes`: Used in `detectron2/export/caffe2_export.py`
    -   `register_custom_op_symbolic`: Used in `detectron2/utils/testing.py`
    -   `unregister_custom_op_symbolic`: Used in `detectron2/utils/testing.py`

-   **torch.onnx.symbolic_helper**:
    -   `torch.onnx.symbolic_helper` (module import): Used in `detectron2/utils/testing.py`
    -   `_onnx_main_opset`: Used in `detectron2/utils/testing.py`
    -   `_onnx_stable_opsets`: Used in `detectron2/utils/testing.py`

-   **torch.onnx.symbolic_opset9**:
    -   `expand`: Used in `detectron2/utils/testing.py`
    -   `unsqueeze`: Used in `detectron2/utils/testing.py`

-   **torch.onnx.symbolic_registry**:
    -   `torch.onnx.symbolic_registry` (module import): Used in `detectron2/utils/testing.py`

-   **torch.onnx.utils**:
    -   `get_ns_op_name_from_custom_op`: Used in `detectron2/utils/testing.py`

-   **torch.optim.lr_scheduler**:
    -   `LRScheduler`: Used in `detectron2/solver/lr_scheduler.py`
    -   `_LRScheduler`: Used in `detectron2/solver/lr_scheduler.py`

-   **torch.utils.checkpoint**:
    -   `torch.utils.checkpoint` (module import): Used in `detectron2/modeling/backbone/swin.py`

-   **torch.utils.collect_env**:
    -   `get_pretty_env_info`: Used in `detectron2/utils/collect_env.py`

-   **torch.utils.cpp_extension**:
    -   `CUDA_HOME`: Used in `detectron2/utils/collect_env.py`
    -   `ROCM_HOME`: Used in `detectron2/utils/collect_env.py`

-   **torch.utils.data**:
    -   `torch.utils.data` (module import): Used in `detectron2/data/build.py`, `detectron2/data/common.py`
    -   `DataLoader`: Used in `inference.py`
    -   `Dataset`: Used in `eval.py`, `inference.py`

-   **torch.utils.data.dataset**:
    -   `Dataset`: Used in `densepose/data/build.py`, `densepose/data/image_list_dataset.py`, `densepose/data/video/video_keyframe_dataset.py`

-   **torch.utils.data.sampler**:
    -   `BatchSampler`: Used in `detectron2/data/samplers/grouped_batch_sampler.py`
    -   `Sampler`: Used in `detectron2/data/common.py`, `detectron2/data/samplers/distributed_sampler.py`, `detectron2/data/samplers/grouped_batch_sampler.py`

-   **torch.utils.tensorboard**:
    -   `SummaryWriter`: Used in `detectron2/utils/events.py`

-   **torchmetrics.image**:
    -   `StructuralSimilarityIndexMeasure`: Used in `eval.py`

-   **torchmetrics.image.lpip**:
    -   `LearnedPerceptualImagePatchSimilarity`: Used in `eval.py`

-   **torchvision**:
    -   `torchvision` (module import): Used in `detectron2/model_zoo/configs/Misc/torchvision_imagenet_R_50.py`, `detectron2/utils/collect_env.py`
    -   `__version__`: Used in `detectron2/layers/roi_align.py`
    -   `transforms`: Used in `eval.py`, `model/SCHP/__init__.py`

-   **torchvision.models.resnet**:
    -   `Bottleneck`: Used in `detectron2/model_zoo/configs/Misc/torchvision_imagenet_R_50.py`
    -   `ResNet`: Used in `detectron2/model_zoo/configs/Misc/torchvision_imagenet_R_50.py`

-   **torchvision.ops**:
    -   `RoIPool`: Used in `detectron2/modeling/poolers.py`
    -   `boxes`: Used in `detectron2/layers/nms.py`
    -   `deform_conv2d`: Used in `detectron2/layers/deform_conv.py`
    -   `nms`: Used in `detectron2/layers/nms.py`
    -   `roi_align`: Used in `detectron2/layers/roi_align.py`

-   **torchvision.transforms**:
    -   `transforms`: Used in `detectron2/model_zoo/configs/Misc/torchvision_imagenet_R_50.py`

-   **tqdm**:
    -   `tqdm` (module import): Used in `detectron2/data/benchmark.py`, `model/pipeline.py`
    -   `tqdm`: Used in `eval.py`, `inference.py`, `preprocess_agnostic_mask.py`, ...

-   **transformers**:
    -   `CLIPImageProcessor`: Used in `model/pipeline.py`
    -   `CLIPTextModel`: Used in `model/utils.py`
    -   `CLIPTokenizer`: Used in `model/utils.py`

-   **types**:
    -   `types` (module import): Used in `detectron2/data/catalog.py`, `detectron2/export/caffe2_modeling.py`

-   **urllib.parse**:
    -   `parse_qs`: Used in `detectron2/checkpoint/detection_checkpoint.py`
    -   `urlparse`: Used in `detectron2/checkpoint/detection_checkpoint.py`

-   **uuid**:
    -   `uuid` (module import): Used in `app_sd_volume.py`, `detectron2/config/lazy.py`

-   **weakref**:
    -   `weakref` (module import): Used in `detectron2/engine/defaults.py`, `detectron2/engine/train_loop.py`

-   **xformers**:
    -   `xformers` (module import): Used in `utils.py`

-   **xml.etree.ElementTree**:
    -   `xml.etree.ElementTree` (module import): Used in `detectron2/data/datasets/pascal_voc.py`, `detectron2/evaluation/pascal_voc_evaluation.py`

-   **yaml**:
    -   `yaml` (module import): Used in `detectron2/config/lazy.py`, `detectron2/utils/env.py`

