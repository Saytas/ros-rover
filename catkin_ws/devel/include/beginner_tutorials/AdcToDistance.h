// Generated by gencpp from file beginner_tutorials/AdcToDistance.msg
// DO NOT EDIT!


#ifndef BEGINNER_TUTORIALS_MESSAGE_ADCTODISTANCE_H
#define BEGINNER_TUTORIALS_MESSAGE_ADCTODISTANCE_H

#include <ros/service_traits.h>


#include <beginner_tutorials/AdcToDistanceRequest.h>
#include <beginner_tutorials/AdcToDistanceResponse.h>


namespace beginner_tutorials
{

struct AdcToDistance
{

typedef AdcToDistanceRequest Request;
typedef AdcToDistanceResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct AdcToDistance
} // namespace beginner_tutorials


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::beginner_tutorials::AdcToDistance > {
  static const char* value()
  {
    return "518d9b1ad9a9efc93a551a303cf3656d";
  }

  static const char* value(const ::beginner_tutorials::AdcToDistance&) { return value(); }
};

template<>
struct DataType< ::beginner_tutorials::AdcToDistance > {
  static const char* value()
  {
    return "beginner_tutorials/AdcToDistance";
  }

  static const char* value(const ::beginner_tutorials::AdcToDistance&) { return value(); }
};


// service_traits::MD5Sum< ::beginner_tutorials::AdcToDistanceRequest> should match 
// service_traits::MD5Sum< ::beginner_tutorials::AdcToDistance > 
template<>
struct MD5Sum< ::beginner_tutorials::AdcToDistanceRequest>
{
  static const char* value()
  {
    return MD5Sum< ::beginner_tutorials::AdcToDistance >::value();
  }
  static const char* value(const ::beginner_tutorials::AdcToDistanceRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::beginner_tutorials::AdcToDistanceRequest> should match 
// service_traits::DataType< ::beginner_tutorials::AdcToDistance > 
template<>
struct DataType< ::beginner_tutorials::AdcToDistanceRequest>
{
  static const char* value()
  {
    return DataType< ::beginner_tutorials::AdcToDistance >::value();
  }
  static const char* value(const ::beginner_tutorials::AdcToDistanceRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::beginner_tutorials::AdcToDistanceResponse> should match 
// service_traits::MD5Sum< ::beginner_tutorials::AdcToDistance > 
template<>
struct MD5Sum< ::beginner_tutorials::AdcToDistanceResponse>
{
  static const char* value()
  {
    return MD5Sum< ::beginner_tutorials::AdcToDistance >::value();
  }
  static const char* value(const ::beginner_tutorials::AdcToDistanceResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::beginner_tutorials::AdcToDistanceResponse> should match 
// service_traits::DataType< ::beginner_tutorials::AdcToDistance > 
template<>
struct DataType< ::beginner_tutorials::AdcToDistanceResponse>
{
  static const char* value()
  {
    return DataType< ::beginner_tutorials::AdcToDistance >::value();
  }
  static const char* value(const ::beginner_tutorials::AdcToDistanceResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // BEGINNER_TUTORIALS_MESSAGE_ADCTODISTANCE_H
