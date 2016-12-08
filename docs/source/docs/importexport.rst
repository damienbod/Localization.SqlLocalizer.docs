Importing and Exporting
=======================================

IStringExtendedLocalizerFactory Import, Export methods
-----------------------

The UpdatetLocalizationData and the AddNewLocalizationData methods of the IStringExtendedLocalizerFactory can be used to import and export data into the database. If these methods are used, the cache is reset. As a user of this interface, you have to implement the logic to decide whether a localization record needs to be updated or added.

.. highlight:: csharp

::

    public interface IStringExtendedLocalizerFactory : IStringLocalizerFactory
    {
        IList GetImportHistory();

        IList GetExportHistory();

        IList GetLocalizationData(string reason = "export");

        IList GetLocalizationData(DateTime from, string culture = null, string reason = "export");

        void UpdatetLocalizationData(List<LocalizationRecord> data, string information);

        void AddNewLocalizationData(List<LocalizationRecord> data, string information);
		
The following example shows how the import, export could be implemented using csv.

https://damienbod.com/2016/07/15/import-export-asp-net-core-localized-data-as-csv/