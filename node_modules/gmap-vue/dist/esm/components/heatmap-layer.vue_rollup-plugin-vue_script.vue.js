import mapElementMixin from '../mixins/map-element.js';
import { heatMapLayerMappedProps } from '../utils/mapped-props-by-map-element.js';
import { getPropsValues, bindProps, bindEvents } from '../utils/helpers.js';

/**
 * HeatmapLayer component
 * @displayName HeatmapLayer
 * @see [source code](/guide/heatmap-layer.html#source-code)
 * @see [Official documentation](https://developers.google.com/maps/documentation/javascript/heatmaplayer)
 */
var script = {
  name: 'HeatmapLayer',
  mixins: [mapElementMixin],
  render() {
    return '';
  },
  provide() {
    const events = [];

    // Infowindow needs this to be immediately available
    const promise = this.$mapPromise
      .then((map) => {
        this.$map = map;

        // Initialize the maps with the given options
        const initialOptions = {
          // TODO: analyze the below line because I think it can be removed
          ...this.options,
          map: this.$map,
          ...getPropsValues(this, heatMapLayerMappedProps),
        };

        const { options: extraOptions, ...finalOptions } = initialOptions;

        this.$heatmapLayerObject = new google.maps.visualization.HeatmapLayer(
          finalOptions
        );

        bindProps(this, this.$heatmapLayerObject, heatMapLayerMappedProps);
        bindEvents(this, this.$heatmapLayerObject, events);

        return this.$heatmapLayerObject;
      })
      .catch((error) => {
        throw error;
      });

    // TODO: analyze the efects of only returns the instance and remove completely the promise
    this.$heatmapLayerPromise = promise;
    return { $heatmapLayerPromise: promise };
  },
  props: {
    /**
     * Extra options that you want to pass to the component
     */
    options: {
      type: Object,
      default: () => {},
    },
    /**
     * The heat map data, is an array of `new google.maps.LatLng`,
     * @see [heatmap options](https://developers.google.com/maps/documentation/javascript/heatmaplayer#add-a-heatmap-layer)
     * @example `[new google.maps.LatLng(37.782, -122.447)]`
     */
    data: {
      type: Array,
      default: undefined,
    },
  },
  destroyed() {
    // Note: not all Google Maps components support maps
    if (this.$heatmapLayerObject && this.$heatmapLayerObject.setMap) {
      this.$heatmapLayerObject.setMap(null);
    }
  },
};

export { script as default };
