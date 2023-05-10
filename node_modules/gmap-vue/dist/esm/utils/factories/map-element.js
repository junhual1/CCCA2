import { objectWithoutProperties as _objectWithoutProperties, objectSpread2 as _objectSpread2, toConsumableArray as _toConsumableArray, defineProperty as _defineProperty } from '../../_virtual/_rollupPluginBabelHelpers.js';
import mapElementMixin from '../../mixins/map-element.js';
import { mappedPropsToVueProps, getPropsValues, bindProps, bindEvents } from '../helpers.js';

var _excluded = ["mappedProps", "name", "ctr", "ctrArgs", "events", "beforeCreate", "afterCreate", "props"],
    _excluded2 = ["options"];
/**
 * Custom assert for local validation
 *
 * @param  {boolean} v The expression that should return a boolean value, if false the assertion fails
 * @param  {string} message Error message to be displayed
 */
// eslint-disable-next-line no-underscore-dangle -- old style should be analyzed

function _assert(v, message) {
  if (!v) throw new Error(message);
}
/**
 * A helper to build your own component for the plugin
 *
 * @param {Object} options
 * @param {Object} options.mappedProps - Definitions of props
 * @param {Object} options.mappedProps.PROP.type - Value type
 * @param {Boolean} options.mappedProps.PROP.twoWay
 *  - Whether the prop has a corresponding PROP_changed
 *   event
 * @param {Boolean} options.mappedProps.PROP.noBind
 *  - If true, do not apply the default bindProps / bindEvents.
 * However it will still be added to the list of component props
 * @param {Object} options.props - Regular Vue-style props.
 *  Note: must be in the Object form because it will be
 *  merged with the `mappedProps`
 *
 * @param {Object} options.events - Google Maps API events
 *  that are not bound to a corresponding prop
 * @param {String} options.name - e.g. `polyline`
 * @param {Function} options.ctr - constructor, e.g.
 *  `google.maps.Polyline`. However, since this is not
 *  generally available during library load, this becomes
 *  a function instead, e.g. () => google.maps.Polyline
 *  which will be called only after the API has been loaded
 *
 *  default: () => String
 *
 * @param {Function} options.ctrArgs -
 *   If the constructor in `ctr` needs to be called with
 *   arguments other than a single `options` object, e.g. for
 *   GroundOverlay, we call `new GroundOverlay(url, bounds, options)`
 *   then pass in a function that returns the argument list as an array
 *
 *   default: (MappedProps, OtherVueProps) => Array
 *
 * Otherwise, the constructor will be called with an `options` object,
 *   with property and values merged from:
 *
 *   1. the `options` property, if any
 *   2. a `map` property with the Google Maps
 *   3. all the properties passed to the component in `mappedProps`
 * @param {Function} options.beforeCreate -
 *  Hook to modify the options passed to the initializer
 *
 *  default: (Object) => Any
 *
 * @param {Function} options.afterCreate -
 *  Hook called when
 *
 *  default: (options.ctr, Object) => Any
 *
 * @returns {Object} A component object that should be exported by default from a Vue component
 */


function mapElement(providedOptions) {
  var mappedProps = providedOptions.mappedProps,
      name = providedOptions.name,
      ctr = providedOptions.ctr,
      ctrArgs = providedOptions.ctrArgs,
      events = providedOptions.events,
      beforeCreate = providedOptions.beforeCreate,
      afterCreate = providedOptions.afterCreate,
      props = providedOptions.props,
      rest = _objectWithoutProperties(providedOptions, _excluded);

  var promiseName = "$".concat(name, "Promise");
  var instanceName = "$".concat(name, "Object");

  _assert(!(props instanceof Array), '`props` should be an object, not Array');

  return _objectSpread2(_objectSpread2({}, typeof GENERATE_DOC !== 'undefined' ? {
    $vgmOptions: providedOptions
  } : {}), {}, {
    mixins: [mapElementMixin],
    props: _objectSpread2(_objectSpread2({}, props), mappedPropsToVueProps(mappedProps)),
    render: function render() {
      return '';
    },
    provide: function provide() {
      var _this = this;

      var promise = this.$mapPromise.then(function (map) {
        // Infowindow needs this to be immediately available
        _this.$map = map; // Initialize the maps with the given options

        var initialOptions = _objectSpread2(_objectSpread2({}, _this.options), {}, {
          map: map
        }, getPropsValues(_this, mappedProps)); // don't use delete keyword in order to create a more predictable code for the engine


        initialOptions.options;
            var finalOptions = _objectWithoutProperties(initialOptions, _excluded2); // delete the extra options


        var options = finalOptions;

        if (beforeCreate) {
          var result = beforeCreate.bind(_this)(options);

          if (result instanceof Promise) {
            return result.then(function () {
              return {
                options: options
              };
            });
          }
        }

        return {
          options: options
        };
      }).then(function (_ref) {
        var _Function$prototype$b;

        var options = _ref.options;
        var ConstructorObject = ctr(); // https://stackoverflow.com/questions/1606797/use-of-apply-with-new-operator-is-this-possible

        _this[instanceName] = ctrArgs ? new ((_Function$prototype$b = Function.prototype.bind).call.apply(_Function$prototype$b, [ConstructorObject, null].concat(_toConsumableArray(ctrArgs(options, getPropsValues(_this, props || {}))))))() : new ConstructorObject(options);
        bindProps(_this, _this[instanceName], mappedProps);
        bindEvents(_this, _this[instanceName], events);

        if (afterCreate) {
          afterCreate.bind(_this)(_this[instanceName]);
        }

        return _this[instanceName];
      });
      this[promiseName] = promise;
      return _defineProperty({}, promiseName, promise);
    },
    destroyed: function destroyed() {
      // Note: not all Google Maps components support maps
      if (this[instanceName] && this[instanceName].setMap) {
        this[instanceName].setMap(null);
      }
    }
  }, rest);
}

export { mapElement as default };
