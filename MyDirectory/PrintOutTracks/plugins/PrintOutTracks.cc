// -*- C++ -*-
//
// Package:    MyDirectory/PrintOutTracks
// Class:      PrintOutTracks
// 
/**\class PrintOutTracks PrintOutTracks.cc MyDirectory/PrintOutTracks/plugins/PrintOutTracks.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Tue, 20 Jan 2015 08:35:58 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

//
// class declaration
//

class PrintOutTracks : public edm::EDAnalyzer {
   public:
      explicit PrintOutTracks(const edm::ParameterSet&);
      ~PrintOutTracks();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

	int i;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
PrintOutTracks::PrintOutTracks(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed

	i = 0;


}


PrintOutTracks::~PrintOutTracks()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
PrintOutTracks::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   std::cout << "Event " << i << std::endl;

   edm::Handle<reco::TrackCollection> tracks;
   iEvent.getByLabel("generalTracks", tracks);

   int j = 0;
   for (reco::TrackCollection::const_iterator track = tracks->begin();  track != tracks->end();  ++track) {
      std::cout << "    Track " << j << " " << track->charge()*track->pt() << " " << track->phi()
                << " " << track->eta() << " " << track->dxy() << " " << track->dz() << std::endl;
      j++;
   }

   i++;


#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
PrintOutTracks::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
PrintOutTracks::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
PrintOutTracks::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
PrintOutTracks::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
PrintOutTracks::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
PrintOutTracks::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
PrintOutTracks::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PrintOutTracks);
