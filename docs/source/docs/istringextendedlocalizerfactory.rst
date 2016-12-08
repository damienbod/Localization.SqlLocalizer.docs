IStringExtendedLocalizerFactory
=======================================

When using the Localization.SqlLocalizer package, the IStringExtendedLocalizerFactory can be used for extra features of this package which are not included in the IStringLocalizerFactory.

.. highlight:: csharp

::

    public interface IStringExtendedLocalizerFactory : IStringLocalizerFactory
    {
        void ResetCache();

        void ResetCache(Type resourceSource);

        IList GetImportHistory();

        IList GetExportHistory();

        IList GetLocalizationData(string reason = "export");

        IList GetLocalizationData(DateTime from, string culture = null, string reason = "export");

        void UpdatetLocalizationData(List<LocalizationRecord> data, string information);

        void AddNewLocalizationData(List<LocalizationRecord> data, string information);

    }
	
.. highlight:: csharp

Example using the interface::

    [Route("api/ImportExport")]
    public class ImportExportController : Controller
    {
        private IStringExtendedLocalizerFactory _stringExtendedLocalizerFactory;

        public ImportExportController(IStringExtendedLocalizerFactory stringExtendedLocalizerFactory)
        {
            _stringExtendedLocalizerFactory = stringExtendedLocalizerFactory;
        }
		
        [HttpGet]
        [Route("localizedData.csv")]
        [Produces("text/csv")]
        public IActionResult GetDataAsCsv()
        {
            return Ok(_stringExtendedLocalizerFactory.GetLocalizationData());
        }
